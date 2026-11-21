#!/usr/bin/env python3
"""Fetch citation counts from OpenAlex and write data/citations.json for Hugo.

Run during the CI build (and optionally locally) before `hugo`. Uses only the
standard library. The output file is gitignored: it is regenerated on every
build, and the site renders fine without it (citation info is simply hidden).

Inputs:
  - params.openalexAuthor in config.yml   -> author-level totals
  - `doi:` front matter in content/papers -> per-paper "Cited by" counts
"""
import datetime
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "citations.json"
API = "https://api.openalex.org"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "academic-site-citations/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def author_id():
    m = re.search(r"^\s*openalexAuthor:\s*['\"]?(A\d+)", (ROOT / "config.yml").read_text(), re.M)
    if not m:
        sys.exit("params.openalexAuthor not set in config.yml")
    return m.group(1)


def paper_dois():
    dois = []
    for f in sorted((ROOT / "content" / "papers").glob("*.md")):
        m = re.search(r'^doi:\s*"?([^"\n]+)"?\s*$', f.read_text(), re.M)
        if m:
            dois.append(m.group(1).strip().lower())
    return dois


def main():
    aid = author_id()
    author = get(f"{API}/authors/{aid}")
    stats = author.get("summary_stats") or {}

    dois = paper_dois()
    works = {}
    if dois:
        flt = urllib.parse.quote("doi:" + "|".join(dois), safe=":|/")
        res = get(f"{API}/works?filter={flt}&per-page=100&select=doi,cited_by_count")
        for w in res.get("results", []):
            doi = (w.get("doi") or "").lower().removeprefix("https://doi.org/")
            if doi:
                works[doi] = w.get("cited_by_count", 0)

    data = {
        "updated": datetime.date.today().isoformat(),
        "source": "OpenAlex",
        "author": {
            "id": aid,
            "url": f"https://openalex.org/authors/{aid}",
            "cited_by": author.get("cited_by_count", 0),
            "h_index": stats.get("h_index", 0),
            "i10_index": stats.get("i10_index", 0),
        },
        "works": works,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    missing = [d for d in dois if d not in works]
    print(f"Wrote {OUT.relative_to(ROOT)}: {data['author']['cited_by']} citations, "
          f"h={data['author']['h_index']}, {len(works)}/{len(dois)} papers matched"
          + (f"; not in OpenAlex: {', '.join(missing)}" if missing else ""))


if __name__ == "__main__":
    main()
