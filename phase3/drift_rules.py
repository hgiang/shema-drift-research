#!/usr/bin/env python3
"""The Phase-3 coding rule: archived prose -> parameter-level units.

This is the rule the lock names (MILESTONES.md "Phase 3 pre-registration"). It is written
to be read and argued with, so every clause is a named pattern and every unit records which
clause decided it. A span qualifies only when it is about a **request** parameter of an
**existing** endpoint; the five SchemaDrift classes are matched independently, two or more
on one parameter make `compound`, and a qualifying span that matches none is `other` — a
unit is never dropped for being unusual, because dropping would bias the prevalence.

`agent_visible` is decided from requiredness and example snippets only, never from the
label, so the two variables cannot contaminate each other.
"""

import re

import entry_text as et

LABELS = ("rename", "enum_tighten", "required", "type_change", "default_change",
          "compound", "other")
TYPES = r"(?:string|integer|int|number|float|boolean|bool|array|list|object|map|enum|timestamp)"

# Each clause is (name, pattern). A span may match clauses from several classes: that is
# what `compound` means. {p} is replaced by the parameter being coded.
CLASSES = {
    "rename": [
        ("renamed-to", r"renam\w*\s+(?:the\s+)?[`\"]?{p}[`\"]?|[`\"]?{p}[`\"]?\s+(?:has\s+been|was|is|were)\s+renam"),
        ("now-called", r"[`\"]?{p}[`\"]?\s+is\s+now\s+called"),
        ("renamed-bare", r"renam\w*\b"),
    ],
    "required": [
        ("now-required", r"[`\"]?{p}[`\"]?[^.]{{0,80}}?\b(?:is|are|becomes?|became)\s+now\s+(?:a\s+)?required"),
        ("now-a-required", r"[`\"]?{p}[`\"]?[^.]{{0,80}}?\bis\s+(?:now\s+)?a\s+required\b"),
        ("endpoint-requires", r"now\s+requires?\s+(?:the\s+)?[`\"]?{p}"),
        ("must-now-pass", r"must\s+now\s+(?:be\s+)?(?:pass|provid|includ|specif|set|send)\w*"),
        ("no-longer-optional", r"[`\"]?{p}[`\"]?[^.]{{0,80}}?no\s+longer\s+optional"),
        ("now-required-bare", r"\bis\s+now\s+(?:a\s+)?required\b"),
    ],
    "enum_tighten": [
        ("value-removed", r"remov\w*\s+(?:the\s+)?[`\"][^`\"]+[`\"]\s+value|remov\w*\s+(?:the\s+)?value"),
        ("no-longer-valid", r"no\s+longer\s+(?:a\s+)?(?:valid|accepted|supported|permitted)\s+value"),
        ("no-longer-accepts", r"no\s+longer\s+accepts?"),
        ("restricted", r"\b(?:restricted|limited)\s+to\b|only\s+accepts?\b"),
        ("allowed-values", r"\b(?:allowed|permitted|valid)\s+values?\b|\benum\b"),
    ],
    "type_change": [
        ("type-changed", r"\btype\s+of\s+[`\"]?{p}[`\"]?[^.]{{0,80}}?(?:chang|is\s+now)|chang\w*\s+the\s+type"),
        ("now-a-type", rf"[`\"]?{{p}}[`\"]?[^.]{{{{0,80}}}}?\bis\s+now\s+(?:an?\s+)?{TYPES}\b"),
        ("now-accepts-type", rf"[`\"]?{{p}}[`\"]?[^.]{{{{0,80}}}}?\bnow\s+accepts?\s+(?:an?\s+)?{TYPES}\b"),
        ("from-type-to-type", rf"\bfrom\s+(?:an?\s+)?{TYPES}\s+to\s+(?:an?\s+)?{TYPES}\b"),
        ("instead-of-type", rf"\binstead\s+of\s+(?:an?\s+)?{TYPES}\b"),
    ],
    "default_change": [
        ("default-for", r"\bdefault\s+(?:value\s+)?(?:for|of)\s+[`\"]?{p}"),
        ("now-defaults", r"[`\"]?{p}[`\"]?[^.]{{0,80}}?\b(?:now\s+defaults?\s+to|defaults?\s+to)\b"),
        ("default-changed", r"\bdefault\b[^.]{{0,80}}?\b(?:chang|is\s+now|was\s+)"),
        ("previously-defaulted", r"\bpreviously\s+default\w*"),
    ],
}

# A span has to be about a request parameter that already exists.
_PARAM_WORD = re.compile(r"\b(parameter|argument|field|property|attribute|option|input|param)s?\b", re.I)
_CHANGE_WORD = re.compile(r"\b(now|no longer|renam\w*|remov\w*|requir\w*|optional|default\w*|"
                          r"chang\w*|replac\w*|deprecat\w*|must|accepts?|tighten\w*|restrict\w*)\b", re.I)
_RESPONSE_ONLY = re.compile(r"\b(response|payload|webhook|event)\b[^.]{0,30}\b(field|object|body|include)|"
                            r"\bin\s+the\s+response\b|\bresponse\s+body\b", re.I)
_BRAND_NEW = re.compile(r"\b(add(?:s|ed|ing)?|introduc\w*|new)\b[^.]{0,20}\bnew\b|"
                        r"\badd(?:s|ed|ing)?\s+(?:a\s+|an\s+)?new\b|\badds?\s+support\s+for\b", re.I)
_EXISTING = re.compile(r"\bexisting\b", re.I)
_EXAMPLE = re.compile(r"[?&]{p}=|[`\"]{p}[`\"]\s*[:=]|^\s*[-+]?\s*[`\"]?{p}[`\"]?\s*:", re.M)


def qualifies(span):
    """True when the span is about a change to a request parameter of an existing endpoint."""
    if not (_PARAM_WORD.search(span) or et.identifiers(span)):
        return False
    if not _CHANGE_WORD.search(span):
        return False
    if _RESPONSE_ONLY.search(span):
        return False
    if _BRAND_NEW.search(span) and not _EXISTING.search(span):
        return False
    return True


_VALUE_LITERAL = re.compile(r"[`\"]([A-Za-z_][\w.-]*)[`\"]\s+(?:value|option|choice)s?\b", re.I)


def parameters_in(span):
    """The parameters a span is *about*.

    Two identifiers in one span are not always two units. A rename names the new name as
    well as the old one, and the unit is the parameter that changed, so only the first
    identifier is kept. An enum clause names the value that went away, which is not a
    parameter at all.
    """
    names = et.identifiers(span)
    values = set(_VALUE_LITERAL.findall(span))
    names = [n for n in names if n not in values]
    if names and any(re.search(pattern.format(p=re.escape(names[0])), span, re.I)
                     for _, pattern in CLASSES["rename"]):
        return names[:1]
    return names


def _matched_clauses(span, parameter):
    out = []
    for label, clauses in CLASSES.items():
        for name, pattern in clauses:
            if re.search(pattern.format(p=re.escape(parameter)), span, re.I):
                out.append((label, name))
                break
    return out


def agent_visible(parameter, span, context=""):
    """True when the parameter is required either side of the change or appears in an
    example request; False when the span says it is optional; None when neither is shown."""
    if re.search(r"\brequired\b", span, re.I):
        return True
    if _EXAMPLE.pattern and re.search(_EXAMPLE.pattern.format(p=re.escape(parameter)),
                                      f"{span}\n{context}", re.I | re.M):
        return True
    if re.search(r"\boptional\b", span, re.I):
        return False
    return None


def classify(span, parameter, context=""):
    """Code one (span, parameter) pair. The label is never dropped for being unusual."""
    matched = _matched_clauses(span, parameter)
    labels = sorted({label for label, _ in matched})
    if len(labels) > 1:
        label, rule = "compound", "compound:" + "+".join(f"{a}.{b}" for a, b in sorted(matched))
    elif labels:
        label, rule = labels[0], f"{matched[0][0]}:{matched[0][1]}"
    else:
        label, rule = "other", "other:qualifies-but-matches-no-class"
    return {"parameter": parameter, "label": label, "classes": labels, "rule": rule,
            "evidence": span, "agent_visible": agent_visible(parameter, span, context)}


def _merge(first, second):
    """Two spans about one parameter: the union of classes, both spans as evidence."""
    classes = sorted(set(first["classes"]) | set(second["classes"]))
    label = "compound" if len(classes) > 1 else (classes[0] if classes else "other")
    visible = first["agent_visible"] if first["agent_visible"] is not None else second["agent_visible"]
    return {**first, "label": label, "classes": classes,
            "rule": f"{first['rule']} | {second['rule']}",
            "evidence": f"{first['evidence']}\n{second['evidence']}", "agent_visible": visible}


def units_of_entry(text):
    """Every qualifying parameter-level unit in one entry, in order of first appearance."""
    units = {}
    for span in et.sentences(text):
        if not qualifies(span):
            continue
        for parameter in parameters_in(span):
            unit = classify(span, parameter, context=text)
            units[parameter] = _merge(units[parameter], unit) if parameter in units else unit
    return list(units.values())
