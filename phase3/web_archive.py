#!/usr/bin/env python3
"""Verbatim web archive for the Phase-3 changelog corpus (MILESTONES.md "Phase 3
pre-registration").

Fetched pages are untrusted data. Everything here treats a response as bytes: it is written
under one archive root, named from a sanitised slug plus an index, recorded in a per-source
manifest (URL, fetch time, status, sha256, size), and never executed, imported or used to
build a command. `archive_path` is the only place a path is built, and it cannot leave the
root whatever the URL says.

Collection is read-only HTTP GET on public documentation: an identifying User-Agent, at
least `MIN_INTERVAL` seconds between requests, `robots.txt` respected, no credentials.
"""

import hashlib
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

MANIFEST = "manifest.json"
SLUG_MAX = 80
FALLBACK_EXT = ".txt"
SAFE_EXT = (".md", ".json", ".html", ".htm", ".txt", ".patch", ".diff", ".xml")
MIN_INTERVAL = 1.0
UA = "schemadrift-research/1.0 (academic study; contact giangdh89@gmail.com)"
TIMEOUT = 60
_UNSAFE = re.compile(r"[^a-z0-9._-]+")


def sha256_bytes(body):
    return hashlib.sha256(body).hexdigest()


def slug(url):
    """A short, lowercase, filesystem-safe name for a URL. Never empty, never a path."""
    path = urllib.parse.urlsplit(url).path
    name = _UNSAFE.sub("-", urllib.parse.unquote(path).lower()).strip("-.")
    name = name.replace("..", "-") or "index"
    return name[-SLUG_MAX:].strip("-.") or "index"


def _extension(url):
    suffix = pathlib.PurePosixPath(urllib.parse.urlsplit(url).path).suffix.lower()
    return suffix if suffix in SAFE_EXT else FALLBACK_EXT


def archive_path(root, source, index, url):
    """<root>/<source>/<index>-<slug><ext>. The only path builder in Phase-3 collection."""
    ext = _extension(url)
    stem = slug(url)
    if stem.endswith(ext.replace(".", "-")) or stem.endswith(ext):
        stem = stem[: -len(ext)].strip("-.") or "index"
    name = f"{int(index):03d}-{stem}"[:SLUG_MAX] + ext
    return pathlib.Path(root) / _UNSAFE.sub("-", str(source).lower()) / name


def _now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def store(root, source, index, url, body, status, now=None):
    """Write the response verbatim and return its manifest entry."""
    path = archive_path(root, source, index, url)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    return {"url": url, "path": path.name, "status": int(status), "n_bytes": len(body),
            "sha256": sha256_bytes(body), "fetched_at": now or _now()}


def load_manifest(root, source):
    path = archive_path(root, source, 0, "x").parent / MANIFEST
    return json.loads(path.read_text()) if path.exists() else {}


def save_manifest(root, source, entries):
    """Sorted by URL so a re-run produces the same bytes."""
    path = archive_path(root, source, 0, "x").parent / MANIFEST
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({k: entries[k] for k in sorted(entries)}, indent=1) + "\n")


def needs_fetch(root, source, manifest, url):
    """False only when the stored file is still the one the manifest recorded."""
    entry = manifest.get(url)
    if not entry:
        return True
    path = archive_path(root, source, 0, "x").parent / entry["path"]
    return not path.exists() or sha256_bytes(path.read_bytes()) != entry["sha256"]


def robots_allows(robots_text, path, agent="*"):
    """Prefix rules of the `User-agent: *` group only; an empty Disallow allows everything."""
    rules, in_group = [], False
    for line in robots_text.splitlines():
        key, _, value = line.split("#")[0].partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            in_group = value == agent
        elif in_group and key in ("disallow", "allow") and value:
            rules.append((key, value))
    match = max((r for r in rules if path.startswith(r[1])), key=lambda r: len(r[1]), default=None)
    return match is None or match[0] == "allow"


class Pacer:
    """At least `min_interval` seconds between requests. The clock is injectable for tests."""

    def __init__(self, min_interval=MIN_INTERVAL, clock=time.monotonic, sleep=time.sleep):
        self._min, self._clock, self._sleep, self._last = min_interval, clock, sleep, None

    def wait(self):
        if self._last is not None:
            gap = self._min - (self._clock() - self._last)
            if gap > 0:
                self._sleep(gap)
        self._last = self._clock()


def http_get(url, timeout=TIMEOUT):
    """GET a public page. Returns (status, bytes); an HTTP error is a status, not an exception."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def fetch_one(root, source, index, url, getter=http_get, allows=None, now=None):
    """Fetch and archive one URL. Returns its manifest entry, or None when skipped.

    Skipped: a path `allows` rejects, or a non-200 response (nothing is stored, so a later
    run retries it). An already-stored, unchanged file is returned without a request.
    """
    manifest = load_manifest(root, source)
    if not needs_fetch(root, source, manifest, url):
        return manifest[url]
    if allows is not None and not allows(urllib.parse.urlsplit(url).path or "/"):
        return None
    status, body = getter(url)
    if status != 200:
        return None
    entry = store(root, source, index, url, body, status, now)
    save_manifest(root, source, {**manifest, url: entry})
    return entry
