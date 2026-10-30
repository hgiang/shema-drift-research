#!/usr/bin/env python3
"""The Phase-3 sampling draw (MILESTONES.md "Phase 3 pre-registration").

Prevalence is the question, so entries are coded in a random order, not newest first. The
order is drawn once per source from a seeded stream and written into the corpus, so the
sample can be rebuilt from the archive alone.

`SEED_P3` is this module's own stream. It is not the analysis RNG (`RNG_P3` in
`analyze.py`); keeping them apart is what `audit_sample.SEED_P2` does for Phase 2.
"""

import zlib

from numpy.random import default_rng

SEED_P3 = 20261030


def _stream(source):
    """One independent stream per source, so adding a source cannot move another's draw."""
    return default_rng([SEED_P3, zlib.crc32(str(source).encode())])


def draw_order(entries, source):
    """A fixed permutation of `entries`, independent of the order they were enumerated in."""
    ordered = sorted(entries)
    index = _stream(source).permutation(len(ordered))
    return [ordered[i] for i in index]
