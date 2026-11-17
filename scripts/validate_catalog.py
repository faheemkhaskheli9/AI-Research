"""Offline structural validation for the curated primary-source catalog."""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "papers" / "catalog.json"
ALLOWED_SOURCE_HOSTS = {
    "arxiv.org", "proceedings.mlr.press", "openreview.net",
    "hai.stanford.edu", "www.nature.com", "www.science.org",
}
REQUIRED = {
    "id", "title", "year", "status", "topics", "url",
    "summary", "open_question", "reviewed_on",
}


def validate(entries: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(entries, list) or not entries:
        return ["catalog must be a nonempty JSON list"]
    ids: set[str] = set()
    for index, entry in enumerate(entries):
        label = f"entry[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label}: must be object")
            continue
        missing = REQUIRED.difference(entry)
        if missing:
            errors.append(f"{label}: missing {sorted(missing)}")
            continue
        if not isinstance(entry["id"], str) or not entry["id"].strip():
            errors.append(f"{label}: invalid id")
        if entry["id"] in ids:
            errors.append(f"{label}: duplicate id {entry['id']}")
        ids.add(entry["id"])
        for field in ("title", "summary", "open_question"):
            if not isinstance(entry[field], str) or not entry[field].strip():
                errors.append(f"{label}: invalid {field}")
        if type(entry["year"]) is not int or not 2000 <= entry["year"] <= date.today().year:
            errors.append(f"{label}: invalid year")
        if entry["status"] not in {"peer_reviewed", "preprint", "research_report"}:
            errors.append(f"{label}: invalid status")
        if not isinstance(entry["topics"], list) or not entry["topics"] or not all(
            isinstance(topic, str) and topic.strip() for topic in entry["topics"]
        ):
            errors.append(f"{label}: invalid topics")
        url = entry["url"]
        if not isinstance(url, str) or (
            urlsplit(url).scheme != "https" or
            urlsplit(url).hostname not in ALLOWED_SOURCE_HOSTS
        ):
            errors.append(f"{label}: non-primary or invalid source URL")
        try:
            reviewed = date.fromisoformat(entry["reviewed_on"])
            if reviewed > date.today() + timedelta(days=1):
                errors.append(f"{label}: review date more than one UTC day in the future")
        except (TypeError, ValueError):
            errors.append(f"{label}: invalid reviewed_on date")
        code_url = entry.get("code_url")
        if code_url is not None and (
            not isinstance(code_url, str) or urlsplit(code_url).scheme != "https"
        ):
            errors.append(f"{label}: invalid code_url")
    return errors


def main() -> None:
    with CATALOG.open(encoding="utf-8") as f:
        catalog = json.load(f)
    errors = validate(catalog)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(catalog)} source-linked papers.")


if __name__ == "__main__":
    main()
