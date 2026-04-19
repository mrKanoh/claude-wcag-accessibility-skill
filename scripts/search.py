#!/usr/bin/env python3
"""
wcag-accessibility skill search utility.

Search the CSV databases by keyword, WCAG level, component, or tool type.

Usage:
  python search.py wcag --level AA
  python search.py wcag --keyword contrast
  python search.py wcag --principle Perceivable
  python search.py aria --component modal
  python search.py aria --keyword button
  python search.py tools --type screen-reader
  python search.py tools --platform Windows
  python search.py tools --free
  python search.py keys --reader NVDA
  python search.py keys --action heading
"""

import csv
import sys
import argparse
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

WCAG_CSV = DATA_DIR / "wcag-criteria.csv"
ARIA_CSV = DATA_DIR / "aria-patterns.csv"
TOOLS_CSV = DATA_DIR / "testing-tools.csv"
KEYS_CSV = DATA_DIR / "screen-reader-keys.csv"
KPIS_CSV = DATA_DIR / "kpis.csv"
MODELS_CSV = DATA_DIR / "disability-models.csv"
TYPOGRAPHY_CSV = DATA_DIR / "typography-rules.csv"
COLOR_CSV = DATA_DIR / "color-palette-rules.csv"
HANDOFF_CSV = DATA_DIR / "handoff-checklist.csv"
SEMANTIC_CSV = DATA_DIR / "semantic-html.csv"
GLOSSARY_CSV = DATA_DIR / "glossary-es.csv"
LEGAL_CSV = DATA_DIR / "legal-framework.csv"


def load_csv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def matches(row: dict, keyword: str) -> bool:
    keyword = keyword.lower()
    return any(keyword in str(v).lower() for v in row.values())


def print_table(rows: list[dict], columns: list[str]) -> None:
    if not rows:
        print("No results found.")
        return

    widths = {col: len(col) for col in columns}
    for row in rows:
        for col in columns:
            widths[col] = max(widths[col], len(str(row.get(col, ""))))

    header = "  ".join(col.ljust(widths[col]) for col in columns)
    separator = "  ".join("-" * widths[col] for col in columns)
    print(header)
    print(separator)
    for row in rows:
        print("  ".join(str(row.get(col, "")).ljust(widths[col]) for col in columns))
    print(f"\n{len(rows)} result(s)")


# ── WCAG ──────────────────────────────────────────────────────────────────────

def cmd_wcag(args: argparse.Namespace) -> None:
    rows = load_csv(WCAG_CSV)

    if args.level:
        rows = [r for r in rows if r["level"].upper() == args.level.upper()]
    if args.principle:
        rows = [r for r in rows if args.principle.lower() in r["principle"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    if args.id:
        rows = [r for r in rows if r["id"].startswith(args.id)]

    print_table(rows, ["id", "level", "principle", "criterion", "description"])

    if args.url and rows:
        print()
        for r in rows:
            print(f"  {r['id']} → {r['url']}")


# ── ARIA ──────────────────────────────────────────────────────────────────────

def cmd_aria(args: argparse.Namespace) -> None:
    rows = load_csv(ARIA_CSV)

    if args.component:
        rows = [r for r in rows if args.component.lower() in r["component"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]

    print_table(rows, ["component", "role", "required_aria", "keyboard", "focus_management"])

    if args.detail and rows:
        print()
        for r in rows:
            print(f"\n── {r['component']} ──")
            for k, v in r.items():
                if v:
                    print(f"  {k}: {v}")


# ── TOOLS ─────────────────────────────────────────────────────────────────────

def cmd_tools(args: argparse.Namespace) -> None:
    rows = load_csv(TOOLS_CSV)

    if args.type:
        rows = [r for r in rows if args.type.lower() in r["type"].lower()]
    if args.platform:
        rows = [r for r in rows if args.platform.lower() in r["platform"].lower()]
    if args.browser:
        rows = [r for r in rows if args.browser.lower() in r["browser"].lower()]
    if args.free:
        rows = [r for r in rows if r["free"].lower().startswith("true")]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]

    print_table(rows, ["tool", "type", "platform", "browser", "free", "best_for"])

    if args.url and rows:
        print()
        for r in rows:
            print(f"  {r['tool']} → {r['url']}")


# ── SCREEN READER KEYS ────────────────────────────────────────────────────────

def cmd_keys(args: argparse.Namespace) -> None:
    rows = load_csv(KEYS_CSV)

    if args.reader:
        rows = [r for r in rows if args.reader.lower() in r["reader"].lower()]
    if args.platform:
        rows = [r for r in rows if args.platform.lower() in r["platform"].lower()]
    if args.mode:
        rows = [r for r in rows if args.mode.lower() in r["mode"].lower()]
    if args.action:
        rows = [r for r in rows if args.action.lower() in r["action"].lower()]

    print_table(rows, ["reader", "platform", "mode", "action", "key"])


# ── KPIs ──────────────────────────────────────────────────────────────────────

def cmd_kpis(args: argparse.Namespace) -> None:
    rows = load_csv(KPIS_CSV)
    if args.category:
        rows = [r for r in rows if args.category.lower() in r["category"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    print_table(rows, ["kpi", "category", "target", "cadence", "formula"])


# ── DISABILITY MODELS ─────────────────────────────────────────────────────────

def cmd_models(args: argparse.Namespace) -> None:
    rows = load_csv(MODELS_CSV)
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    print_table(rows, ["model", "focus", "view_of_disability", "design_implication"])


# ── TYPOGRAPHY ────────────────────────────────────────────────────────────────

def cmd_typography(args: argparse.Namespace) -> None:
    rows = load_csv(TYPOGRAPHY_CSV)
    if args.category:
        rows = [r for r in rows if args.category.lower() in r["category"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    print_table(rows, ["rule", "category", "recommendation", "wcag_ref"])


# ── COLOR PALETTE ─────────────────────────────────────────────────────────────

def cmd_color(args: argparse.Namespace) -> None:
    rows = load_csv(COLOR_CSV)
    if args.scope:
        rows = [r for r in rows if args.scope.lower() in r["scope"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    print_table(rows, ["rule", "scope", "recommendation", "wcag_ref", "tool"])


# ── HANDOFF ───────────────────────────────────────────────────────────────────

def cmd_handoff(args: argparse.Namespace) -> None:
    rows = load_csv(HANDOFF_CSV)
    if args.phase:
        rows = [r for r in rows if args.phase.lower() in r["phase"].lower()]
    if args.owner:
        rows = [r for r in rows if args.owner.lower() in r["owner"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    print_table(rows, ["phase", "owner", "item", "artifact"])


# ── SEMANTIC HTML ─────────────────────────────────────────────────────────────

def cmd_semantic(args: argparse.Namespace) -> None:
    rows = load_csv(SEMANTIC_CSV)
    if args.element:
        rows = [r for r in rows if args.element.lower() in r["element"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    print_table(rows, ["element", "role", "use_for", "avoid_when"])


# ── GLOSSARY (ES↔EN) ─────────────────────────────────────────────────────────

def cmd_glossary(args: argparse.Namespace) -> None:
    rows = load_csv(GLOSSARY_CSV)
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    if args.context:
        rows = [r for r in rows if args.context.lower() in r["contexto"].lower()]
    print_table(rows, ["en", "es", "definicion", "contexto"])


# ── LEGAL FRAMEWORK ────────────────────────────────────────────────────────────

def cmd_legal(args: argparse.Namespace) -> None:
    rows = load_csv(LEGAL_CSV)
    if args.jurisdiction:
        rows = [r for r in rows if args.jurisdiction.lower() in r["jurisdiction"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    print_table(rows, ["jurisdiction", "law", "standard_referenced", "effective", "scope"])


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search the WCAG Accessibility skill databases.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # wcag subcommand
    p_wcag = sub.add_parser("wcag", help="Search WCAG criteria")
    p_wcag.add_argument("--level", help="A, AA, or AAA")
    p_wcag.add_argument("--principle", help="Perceivable / Operable / Understandable / Robust")
    p_wcag.add_argument("--keyword", help="Search across all fields")
    p_wcag.add_argument("--id", help="Criterion ID prefix (e.g. 1.4 or 2.1.1)")
    p_wcag.add_argument("--url", action="store_true", help="Show understanding URLs")

    # aria subcommand
    p_aria = sub.add_parser("aria", help="Search ARIA component patterns")
    p_aria.add_argument("--component", help="Component name (e.g. modal, button, tabs)")
    p_aria.add_argument("--keyword", help="Search across all fields")
    p_aria.add_argument("--detail", action="store_true", help="Show full detail for each result")

    # tools subcommand
    p_tools = sub.add_parser("tools", help="Search testing tools")
    p_tools.add_argument("--type", help="browser-extension / cli / screen-reader / mobile / color / testing-library / bookmarklet / ci / validator")
    p_tools.add_argument("--platform", help="Windows / macOS / Android / iOS / Any")
    p_tools.add_argument("--browser", help="Chrome / Firefox / Edge / Safari / Any")
    p_tools.add_argument("--free", action="store_true", help="Free tools only")
    p_tools.add_argument("--keyword", help="Search across all fields")
    p_tools.add_argument("--url", action="store_true", help="Show tool URLs")

    # keys subcommand
    p_keys = sub.add_parser("keys", help="Search screen reader keyboard shortcuts")
    p_keys.add_argument("--reader", help="NVDA / JAWS / VoiceOver / TalkBack / Narrator")
    p_keys.add_argument("--platform", help="Windows / macOS / iOS / Android")
    p_keys.add_argument("--mode", help="Browse / Forms / Table / General / Web")
    p_keys.add_argument("--action", help="Keyword in action name (e.g. heading, link, table)")

    # kpis subcommand
    p_kpis = sub.add_parser("kpis", help="Search accessibility KPIs")
    p_kpis.add_argument("--category", help="Technical / Conformance / Remediation / User Outcome / Visual / Design System / Process / Organization / Regression / Feedback / Compliance / Perceivable")
    p_kpis.add_argument("--keyword", help="Search across all fields")

    # disability models subcommand
    p_models = sub.add_parser("models", help="Search theoretical models of disability")
    p_models.add_argument("--keyword", help="Search across all fields")

    # typography subcommand
    p_type = sub.add_parser("typography", help="Search accessible typography rules")
    p_type.add_argument("--category", help="Size / Spacing / Layout / Responsive / Contrast / Meaning / Technical / Style / Weight / Face / Perceivable / Links")
    p_type.add_argument("--keyword", help="Search across all fields")

    # color subcommand
    p_color = sub.add_parser("color", help="Search color palette rules")
    p_color.add_argument("--scope", help="Text / Non-text / Meaning / System / Theme / Charts / Brand / Backgrounds / Design tokens / Disabled / Windows / Perception / Differentiation / Alternate media / Links")
    p_color.add_argument("--keyword", help="Search across all fields")

    # handoff subcommand
    p_hand = sub.add_parser("handoff", help="Search design-to-dev a11y handoff checklist")
    p_hand.add_argument("--phase", help="Research / Design / Development / QA / Release")
    p_hand.add_argument("--owner", help="UX / Designer / Dev / QA / PM / Content / Compliance")
    p_hand.add_argument("--keyword", help="Search across all fields")

    # semantic HTML subcommand
    p_sem = sub.add_parser("semantic", help="Search semantic HTML element reference")
    p_sem.add_argument("--element", help="Element name (e.g. nav, button, table)")
    p_sem.add_argument("--keyword", help="Search across all fields")

    # glossary subcommand
    p_gloss = sub.add_parser("glossary", help="Spanish <-> English accessibility glossary")
    p_gloss.add_argument("--keyword", help="Search term in English or Spanish")
    p_gloss.add_argument("--context", help="Context category (e.g. ARIA / Legal / AT / Teclado)")

    # legal subcommand
    p_legal = sub.add_parser("legal", help="Legal frameworks by jurisdiction")
    p_legal.add_argument("--jurisdiction", help="Country or region (e.g. Spain, Brazil, EU, US)")
    p_legal.add_argument("--keyword", help="Search across all fields")

    args = parser.parse_args()

    dispatch = {
        "wcag": cmd_wcag,
        "aria": cmd_aria,
        "tools": cmd_tools,
        "keys": cmd_keys,
        "kpis": cmd_kpis,
        "models": cmd_models,
        "typography": cmd_typography,
        "color": cmd_color,
        "handoff": cmd_handoff,
        "semantic": cmd_semantic,
        "glossary": cmd_glossary,
        "legal": cmd_legal,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
