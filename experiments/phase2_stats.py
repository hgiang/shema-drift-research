#!/usr/bin/env python3
"""Phase-2 verdicts P10-P16: pure functions, no file I/O, no randomness.

Implements the locked pre-registration (MILESTONES.md "Phase 2 pre-registration") with the
Phase-1 rules it carries over (phase1_stats: unlock rule, noise floor). Each verdict is
{"holds": True | False | None (arm incomplete or not run), "basis": str}. An undefined
recovery (A - B_strict <= 0: no drop to recover) leaves a verdict pending, as Phase 1's P4.
"""

import phase1_stats as st

SONNET, HAIKU = "anthropic/claude-sonnet-5.5", "anthropic/claude-haiku-5.5"
LLAMA = "meta-llama/llama-3.3-70b-instruct"
FLASH = "gemini-3.6-flash"
CLAUDE = (HAIKU, SONNET)
NEW_FAMILIES = (SONNET, HAIKU, LLAMA)  # this order fixes the RNG_P2 draws
P11_MIN_GAIN = 0.30  # C:user:prose:apply - C, in recovery units
P12_MIN_GAIN = 0.30  # D' - D on newly-required (P5 extended)
P14_MIN_GAIN, P14_BAND = 0.30, 0.10
P16_MIN = 0.95


def _unlock_status(c):
    """Phase-1 unlock rule for one family's C: None while recovery is undefined, False on any
    failed criterion, None while the noise floor is pending, else whether it clears the floor."""
    if c["recovery"] is None:
        return None
    if c["recovery"] < st.UNLOCK_RECOVERY or c["ci_low"] <= 0 or not c["bh"]:
        return False
    if c["floor"] is None:
        return None
    return not st.within_noise(c["mean"], c["floor"])


def p10(claude):
    status = {m: _unlock_status(claude[m]) for m in CLAUDE if m in claude}
    if False in status.values():
        holds = False
    else:
        holds = True if len(status) == len(CLAUDE) and all(status.values()) else None
    return {"holds": holds, "basis": f"C unlocks recovery on all 120 pairs: {status}"}


def p11(llama):
    if llama is None:
        return {"holds": None, "basis": "Llama core, placement or noise arm incomplete"}
    if llama["c_recovery"] is None or llama["gain"] is None:
        return {"holds": None, "basis": "no drop to recover (A - B_strict <= 0): recovery undefined"}
    basis = (f"C recovery {llama['c_recovery']:.3f} (needs < {st.UNLOCK_RECOVERY}), placement - C "
             f"{llama['gain']:+.3f} recovery units (needs >= {P11_MIN_GAIN}), BH {llama['bh']}, "
             f"paired mean {llama['mean']:+.3f}, noise floor {llama['floor']}")
    if llama["c_recovery"] >= st.UNLOCK_RECOVERY or llama["gain"] < P11_MIN_GAIN or not llama["bh"]:
        return {"holds": False, "basis": basis}
    if llama["floor"] is None:
        return {"holds": None, "basis": basis}
    return {"holds": not st.within_noise(llama["mean"], llama["floor"]), "basis": basis}


def _families(stats, key):
    fam = stats.get("families") or {}
    return {f: fam[f][key] for f in NEW_FAMILIES if f in fam and key in fam[f]}


def p12(stats):
    got = _families(stats, "Dprime-D_required")
    fails = [f for f, s in got.items() if s["mean"] < P12_MIN_GAIN]
    holds = False if fails else (True if len(got) == len(NEW_FAMILIES) else None)
    return {"holds": holds, "basis": f"D' - D on required, means {({f: round(s['mean'], 3) for f, s in got.items()})}; "
                                     f"needs >= {P12_MIN_GAIN} in all {len(NEW_FAMILIES)} new families"}


def p13(stats):
    keys = ("CD-C", "CD-D")
    below = sorted({f for k in keys for f, s in _families(stats, k).items() if s["ci95"][1] < 0})
    complete = all(len(_families(stats, k)) == len(NEW_FAMILIES) for k in keys)
    holds = False if below else (True if complete else None)
    return {"holds": holds, "basis": f"new families with a C+D CI wholly below 0: {below or 'none'} (pin A7)"}


def p14(fill):
    if fill is None:
        return {"holds": None, "basis": "Flash fill arm incomplete"}
    info, lo_hi = fill["info"], fill["contrast"]["ci95"]
    gain = (info["mean"] >= P14_MIN_GAIN and info["ci95"][0] > 0 and info["bh"]
            and not st.within_noise(info["mean"], fill["floor"]))
    flat = -P14_BAND <= lo_hi[0] and lo_hi[1] <= P14_BAND
    return {"holds": bool(gain and flat),
            "basis": f"B_fill - B_strict on required+default {info['mean']:+.3f} CI {info['ci95']} BH {info['bh']} "
                     f"(needs >= {P14_MIN_GAIN}, noise floor {fill['floor']}); on the contrast set CI {lo_hi} "
                     f"(needs inside [-{P14_BAND}, {P14_BAND}])"}


def p15(direct):
    if direct.get("run"):
        raise ValueError("the direct arm ran, but P15 scoring is not implemented (the probe found no lift)")
    return {"holds": None, "basis": f"direct arm not run: {direct['basis']}"}


def p16(replay):
    if replay is None:
        return {"holds": None, "basis": "validator replay file missing"}
    rates = {"pydantic_default~lenient": replay["pydantic_default"]["vs_lenient"],
             "fastapi_default~lenient": replay["fastapi_default"]["vs_lenient"],
             "jsonschema_closed~strict": replay["jsonschema_closed"]["vs_strict"]}
    return {"holds": all(r >= P16_MIN for r in rates.values()),
            "basis": f"agreement {rates}; each needs >= {P16_MIN} (descriptive, not in BH)"}


def verdicts(stats):
    """P10-P16 judged by code."""
    return {"P10": p10(stats["claude"]), "P11": p11(stats["llama"]), "P12": p12(stats), "P13": p13(stats),
            "P14": p14(stats["fill"]), "P15": p15(stats["direct"]), "P16": p16(stats["replay"])}
