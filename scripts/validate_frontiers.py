"""Validate frontier study inventory against cited catalog and Markdown reviews.

Checks structural completeness only, not whether source claims are independently reproduced.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research" / "areas" / "index.json"
PAPERS = ROOT / "papers" / "catalog.json"

REQUIRED_SECTIONS = (
    "## State of research through November 2026",
    "## Open research problems",
    "## Candidate hypothesis",
    "## Proposed experiment",
    "## Adversarial review",
)


def validate_frontiers(records: object, paper_ids: set[str], base: Path) -> list[str]:
    errors: list[str] = []
    if not isinstance(records, list) or len(records) != 12:
        return ["frontier registry must contain exactly 12 area records"]
    seen: set[str] = set()
    for i, record in enumerate(records, start=1):
        label = f"frontier[{i}]"
        if not isinstance(record, dict):
            errors.append(f"{label}: not an object")
            continue
        if record.get("id") != f"{i:02d}":
            errors.append(f"{label}: unexpected ordered id")
        slug = record.get("slug")
        if not isinstance(slug, str) or slug != f"{i:02d}-{slug[3:]}" or not slug[3:].replace("-", "").isalnum():
            errors.append(f"{label}: invalid slug")
            continue
        if slug in seen:
            errors.append(f"{label}: duplicate slug")
        seen.add(slug)
        path = f"research/areas/{slug}.md"
        if record.get("review_path") != path:
            errors.append(f"{label}: review path mismatch")
        review_file = base / path
        if not review_file.is_file():
            errors.append(f"{label}: review missing")
            continue
        content = review_file.read_text(encoding="utf-8")
        for heading in REQUIRED_SECTIONS:
            # Reviews 01–06 use slightly different headings from reviews 07–12.
            equivalent = {
                "## State of research through November 2026": (
                    "## State of research through November 2026",
                ),
                "## Open research problems": (
                    "## Open research problems", "## Open gaps worth testing",
                ),
                "## Candidate hypothesis": (
                    "## Candidate hypothesis", "## Falsifiable research hypothesis",
                ),
                "## Proposed experiment": (
                    "## Proposed experiment", "## Experimental design",
                ),
                "## Adversarial review": (
                    "## Adversarial review", "## Adversarial review / likely failure",
                ),
            }[heading]
            if not any(x in content for x in equivalent):
                errors.append(f"{label}: missing heading {heading}")
        refs = record.get("key_paper_ids")
        if not isinstance(refs, list) or len(refs) < 3:
            errors.append(f"{label}: expected >=3 paper refs")
        else:
            unknown = sorted(set(refs) - paper_ids)
            if unknown:
                errors.append(f"{label}: unknown paper references {unknown}")
        if record.get("experiment_status") != "proposed_not_executed":
            errors.append(f"{label}: unexpected experiment status")
        if len(content) < 1500:
            errors.append(f"{label}: review too brief")
    return errors


def main() -> None:
    records = json.loads(REGISTRY.read_text(encoding="utf-8"))
    papers = json.loads(PAPERS.read_text(encoding="utf-8"))
    errors = validate_frontiers(records, {x["id"] for x in papers}, ROOT)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(records)} source-linked frontier research proposals.")


if __name__ == "__main__":
    main()
