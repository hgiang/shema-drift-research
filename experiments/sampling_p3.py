#!/usr/bin/env python3
"""The Phase-3 draws for the catalog arm (MILESTONES.md "Phase 3 pre-registration").

Two draws, each from its own stream so adding one cannot move the other:
  * which 40 of the 120 primary pairs the arm runs, 8 per drift class;
  * the order the 30 frozen tools are declared in, which fixes where the drifted tool sits.

`SEED_P3` is this module's own stream, kept apart from the analysis RNG in `analyze.py`,
exactly as `audit_sample.SEED_P2` is for Phase 2.
"""

import collections
import zlib

from numpy.random import default_rng

SEED_P3 = 20261030


def _stream(name):
    return default_rng([SEED_P3, zlib.crc32(str(name).encode())])


def draw_pairs(pairs, per_class):
    """`per_class` pairs from each drift class, drawn without replacement, order fixed."""
    by_class = collections.defaultdict(list)
    for task, drift_class in sorted(pairs, key=lambda p: (p[1], p[0]["id"])):
        by_class[drift_class].append((task, drift_class))
    out = []
    for drift_class in sorted(by_class):
        group = by_class[drift_class]
        index = _stream(f"pairs:{drift_class}").permutation(len(group))[:per_class]
        out += [group[i] for i in sorted(index)]
    return out


def draw_catalog_order(names):
    """One fixed declaration order for the whole arm."""
    ordered = sorted(names)
    index = _stream("catalog").permutation(len(ordered))
    return [ordered[i] for i in index]
