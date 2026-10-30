#!/usr/bin/env python3
"""Phase-3 corpus verdicts P17-P20: pure functions, no file I/O, no randomness.

Implements the locked rule (MILESTONES.md "Phase 3 pre-registration"): each prediction is a
share against a threshold, and the verdict comes from the 95% bootstrap CI, never from the
point estimate alone.

  holds  the CI lies wholly on the predicted side of the threshold
  fails  it lies wholly on the other side
  None   it straddles the threshold: the corpus cannot decide at this size

A corpus too small to separate the two is reported undecided, not argued either way.
"""

FIVE = ("rename", "enum_tighten", "required", "type_change", "default_change")
COVERED = FIVE + ("compound",)
COSTLY = ("required", "default_change")
P17_MIN = 0.70   # the five classes plus compound cover this much of the corpus
P18_MIN = 0.20   # required + default_change
P19_MIN = 0.50   # agent_visible among units with a decided value
P20_MIN = 0.10   # compound


def verdict(share, threshold, basis):
    """One prediction of the form `share >= threshold`, judged on the CI."""
    if share is None or share.get("ci95") is None or not share.get("n"):
        return {"holds": None, "basis": f"{basis}: no units to score"}
    low, high = share["ci95"]
    if low >= threshold:
        holds = True
    elif high < threshold:
        holds = False
    else:
        holds = None
    return {"holds": holds,
            "basis": f"{basis} {share['point']:.3f} CI [{low:.3f}, {high:.3f}] "
                     f"on n={share['n']}; needs >= {threshold}"}


def verdicts(shares):
    """P17-P20 judged by code."""
    return {
        "P17": verdict(shares.get("coverage"), P17_MIN,
                       "share of units in the five classes or compound"),
        "P18": verdict(shares.get("costly"), P18_MIN,
                       "share of units that are required or default_change"),
        "P19": verdict(shares.get("reach"), P19_MIN,
                       "share of decided units that are agent_visible"),
        "P20": verdict(shares.get("compound"), P20_MIN, "share of units that are compound"),
    }
