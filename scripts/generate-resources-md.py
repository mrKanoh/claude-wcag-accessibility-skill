#!/usr/bin/env python3
"""
Generate RESOURCES.md from data/resources.csv.

Run from the skill root:
  python scripts/generate-resources-md.py

Reads data/resources.csv and writes RESOURCES.md with resources grouped
by Category, then sorted by Year (desc) within each group.
"""

import csv
from pathlib import Path
from datetime import date

ROOT     = Path(__file__).parent.parent
CSV_PATH = ROOT / "data" / "resources.csv"
OUT_PATH = ROOT / "RESOURCES.md"

CATEGORY_ICONS = {
    "Official Standards":  "📐",
    "Practical Guides":    "🛠️",
    "Blogs":               "📝",
    "Research":            "🔬",
    "Tools":               "⚙️",
    "Libraries":           "📦",
    "Books":               "📚",
    "Communities":         "🤝",
    "Legal":               "⚖️",
    "Case Studies":        "📊",
}


def load_resources() -> list[dict]:
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def group_by_category(rows: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for row in rows:
        cat = row.get("Category", "Other").strip()
        groups.setdefault(cat, []).append(row)
    # Sort within each category: newest first, then alphabetically
    for cat in groups:
        groups[cat].sort(key=lambda r: (-int(r.get("Year", "0") or 0), r.get("Title", "")))
    return groups


def render_row(row: dict) -> str:
    title     = row.get("Title", "").strip()
    url       = row.get("URL", "").strip()
    authority = row.get("Authority", "").strip()
    year      = row.get("Year", "").strip()
    type_     = row.get("Type", "").strip()
    language  = row.get("Language", "EN").strip()
    notes     = row.get("Notes", "").strip()

    # Build link
    link = f"[{title}]({url})" if url else title

    # Build meta line
    meta_parts = []
    if authority:
        meta_parts.append(f"**{authority}**")
    if year:
        meta_parts.append(year)
    if type_:
        meta_parts.append(f"_{type_}_")
    if language and language.upper() != "EN":
        meta_parts.append(f"`{language}`")

    meta = " · ".join(meta_parts)
    line = f"- {link}"
    if meta:
        line += f" — {meta}"
    if notes:
        line += f"  \n  {notes}"
    return line


def build_md(groups: dict[str, list[dict]]) -> str:
    today = date.today().isoformat()
    lines = [
        "# Accessibility Resources",
        "",
        f"> Auto-generated from `data/resources.csv` on {today}.",
        "> To add a resource, edit the CSV and re-run `python scripts/generate-resources-md.py`.",
        "",
        "## Table of Contents",
        "",
    ]

    for cat in groups:
        icon = CATEGORY_ICONS.get(cat, "📌")
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("/", "")
        lines.append(f"- [{icon} {cat}](#{anchor})")

    lines.append("")
    lines.append("---")
    lines.append("")

    for cat, rows in groups.items():
        icon = CATEGORY_ICONS.get(cat, "📌")
        lines.append(f"## {icon} {cat}")
        lines.append("")
        for row in rows:
            lines.append(render_row(row))
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append(
        "*This file is auto-generated. "
        "To contribute a resource, add a row to `data/resources.csv` and open a PR.*"
    )
    return "\n".join(lines)


def main() -> None:
    rows = load_resources()
    groups = group_by_category(rows)
    md = build_md(groups)
    OUT_PATH.write_text(md, encoding="utf-8")
    print(f"✅ Written {len(rows)} resources across {len(groups)} categories → {OUT_PATH}")


if __name__ == "__main__":
    main()
