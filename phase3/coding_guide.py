#!/usr/bin/env python3
"""The coding guide the two blind coders read, and the parser for what they return
(MILESTONES.md "Phase 3 pre-registration" and "Phase 3 amendment 1").

The guide quotes the locked definitions and **nothing else**. It never names a prediction,
never says which labels the study expects to be common, and never shows a proportion: a
coder who could guess the hypothesis would not be a blind coder.
"""

import json
import re

LABELS = ("rename", "enum_tighten", "required", "type_change", "default_change",
          "compound", "other")

GUIDE = """You are coding entries from public API changelogs for a study of how API schemas change.
Work only from the text you are given. Do not guess beyond it, and do not look anything up.

A UNIT is one parameter-level change to one existing endpoint or tool.
An entry that changes two parameters gives two units. An entry that changes one parameter in
two ways gives one unit.

A unit QUALIFIES when a REQUEST parameter of an EXISTING endpoint or tool changes its
name, type, allowed values, requiredness, or default.

Exclude, and return no unit for:
- response-only changes (fields in a response, payload, webhook or event body);
- brand-new endpoints, tools or parameters that add no constraint to an existing call;
- pure documentation wording;
- deprecation notices that take effect outside 2023-01-01 to 2026-09-30;
- changes to authentication, rate limits, pagination envelopes or transport.

Give each qualifying unit EXACTLY ONE label:
- "rename"          the parameter's name changed
- "enum_tighten"    the set of values the parameter accepts got smaller
- "required"        a parameter that was optional became required
- "type_change"     the parameter's type changed
- "default_change"  the parameter's default value changed
- "compound"        two or more of the five above, on the same parameter, in one release
- "other"           it qualifies under the rule above but is none of the five

Four cases the labels above do not settle on their own:
- A parameter that is REMOVED is "rename" when the entry names the parameter that replaces
  it, and "other" when no replacement is named.
- A parameter that became optional is the opposite of "required", so it is "other".
- A newly added required parameter on an existing endpoint qualifies, because a new required
  parameter is a constraint on a call that already exists, and its label is "required".
- Conditional requiredness ("when you set X you must also set Y") is "required".
- A value set that becomes an enum, replacing a free-form or boolean value, is both a smaller
  value set and a type change on the same parameter in one release, so it is "compound".

Also give each unit AGENT_VISIBLE, decided WITHOUT looking at the label you just chose:
- true   the parameter is required either before or after the change, OR it appears in an
         example request shown in the entry
- false  the entry says the parameter is optional and shows no example using it
- null   neither is shown

The candidate spans and identifiers below are suggestions from a crude text filter. They are
often wrong: many are not parameters at all (error codes, command names, plan names, file
names, string literals from code). Reject anything that is not a request parameter, and add a
parameter the filter missed if the text clearly shows one.

Answer with JSON only, no prose and no code fence: a JSON array with one object per digest,
in the order the digests are given:
[{"digest_id": "<id>", "units": [{"parameter": "<name>", "label": "<one of the labels>",
"agent_visible": true|false|null}]}]
An entry with no qualifying unit gets "units": [].
"""

_FENCE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$", re.M)


def prompt_for(batch):
    """The guide plus one batch of digests, as the coder sees it."""
    body = "\n".join(json.dumps(d, ensure_ascii=False) for d in batch)
    return f"{GUIDE}\nDIGESTS ({len(batch)}):\n{body}\n"


def parse(answer, batch):
    """Parse one coder answer into units. Unknown labels and stray digest ids are dropped.

    Returns (units, problems): a coder that answers badly is reported, never silently fixed.
    """
    ids = {d["digest_id"] for d in batch}
    text = _FENCE.sub("", answer.strip())
    start, end = text.find("["), text.rfind("]")
    if start < 0 or end < start:
        return [], [f"no JSON array in the answer for {sorted(ids)}"]
    try:
        rows = json.loads(text[start:end + 1])
    except json.JSONDecodeError as e:
        return [], [f"unparsable JSON for {sorted(ids)}: {e}"]
    units, problems = [], []
    for row in rows if isinstance(rows, list) else []:
        digest_id = (row or {}).get("digest_id")
        if digest_id not in ids:
            problems.append(f"unknown digest_id {digest_id!r}")
            continue
        for unit in row.get("units") or []:
            label, parameter = unit.get("label"), unit.get("parameter")
            if label not in LABELS or not parameter:
                problems.append(f"{digest_id}: bad unit {unit!r}")
                continue
            visible = unit.get("agent_visible")
            units.append({"digest_id": digest_id, "parameter": str(parameter), "label": label,
                          "agent_visible": visible if isinstance(visible, bool) else None})
    missing = ids - {r.get("digest_id") for r in rows if isinstance(r, dict)}
    problems += [f"no answer for {d}" for d in sorted(missing)]
    return units, problems
