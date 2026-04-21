# Contributing to claude-wcag-accessibility-skill

Thank you for helping improve this skill! Every contribution — fixes, new patterns,
better prompts, corrected CSV data — makes a real difference for developers building
accessible products.

---

## Table of Contents

- [Types of contributions](#types-of-contributions)
- [Getting started](#getting-started)
- [Project structure](#project-structure)
- [CSV database conventions](#csv-database-conventions)
- [Adding a component example](#adding-a-component-example)
- [Adding or improving a prompt](#adding-or-improving-a-prompt)
- [Improving SKILL.md](#improving-skillmd)
- [Commit conventions](#commit-conventions)
- [Pull request checklist](#pull-request-checklist)
- [Code of conduct](#code-of-conduct)

---

## Types of contributions

| Type | Where | Notes |
|------|-------|-------|
| Bug fix in a CSV (wrong WCAG SC, typo) | `data/*.csv` | Reference the correct SC or spec |
| New ARIA pattern | `data/aria-patterns.csv` + `examples/components/` | Must include keyboard + focus behavior |
| New accessible component | `examples/components/` | HTML-vanilla first; full keyboard + SR support |
| New/improved Claude prompt | `prompts/` | Follow the prompt template format |
| New jurisdiction in legal framework | `data/legal-framework.csv` | Include law name, standard, effective date, scope |
| New glossary term (ES↔EN) | `data/glossary-es.csv` | Include context field |
| SKILL.md improvement | `SKILL.md` | Keep sections ≤ 500 lines total; add to existing section if possible |
| New template | `templates/` | Include usage instructions inside the file |
| search.py improvement | `scripts/search.py` | Include tests in `tests/test_search.py` |
| Documentation | `README.md`, `RESOURCES.md` | Keep in sync with actual file structure |

---

## Getting started

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/claude-wcag-accessibility-skill.git
cd claude-wcag-accessibility-skill

# 2. (Optional) Set up Python environment for search.py + tests
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install pytest

# 3. Verify tests pass
pytest tests/ -v

# 4. Create a feature branch
git checkout -b feat/your-improvement-description

# 5. Make your changes, commit, and push
git push origin feat/your-improvement-description

# 6. Open a Pull Request against main
```

---

## Project structure

```
wcag-accessibility/
├── SKILL.md                    ← Claude skill (auto-loaded by Claude Code)
├── README.md                   ← Project docs — KEEP IN SYNC with actual files
├── CHANGELOG.md                ← Document your changes here
├── CONTRIBUTING.md             ← This file
│
├── data/                       ← 14 searchable CSV databases
│   ├── wcag-criteria.csv
│   ├── aria-patterns.csv
│   ├── cognitive-accessibility.csv   ← COGA patterns
│   └── ...
│
├── examples/
│   └── components/             ← Working HTML demos (keyboard + screen-reader tested)
│       ├── date-picker.html
│       ├── toast-notifications.html
│       ├── carousel.html
│       └── tree-view.html
│
├── prompts/                    ← 12 Claude prompts
├── templates/                  ← Audit report, CI pipeline, VPAT
├── scripts/
│   ├── search.py               ← CLI search tool
│   └── generate-resources-md.py
└── tests/
    └── test_search.py          ← pytest suite for search.py
```

---

## CSV database conventions

Each CSV has a consistent header row. **Do not add or rename columns** without updating
`scripts/search.py` and documenting the change in `CHANGELOG.md`.

### wcag-criteria.csv columns
`id, level, principle, criterion, description, url`

### aria-patterns.csv columns
`component, role, required_aria, optional_aria, keyboard, focus_management, notes, example_url`

### cognitive-accessibility.csv columns
`pattern_id, pattern_name, user_group, wcag_ref, coga_objective, description, design_guidance, implementation_notes, testing_notes`

### General rules
- Use UTF-8 encoding
- Wrap fields containing commas in double quotes
- Keep descriptions concise (one sentence per field where possible)
- Always reference a WCAG SC when applicable (`1.4.3`, `2.1.1`, etc.)

---

## Adding a component example

Component examples live in `examples/components/` as self-contained HTML files.

### Requirements checklist

Before submitting, verify your component:

- [ ] Works with **keyboard only** (Tab, Enter, Space, Arrow keys, Escape where applicable)
- [ ] Has been tested with **NVDA + Firefox** (Windows)
- [ ] Has been tested with **VoiceOver + Safari** (macOS) OR TalkBack
- [ ] Uses correct **ARIA roles, states, and properties** per the WAI-ARIA APG
- [ ] Has a **visible focus indicator** (≥ 3:1 contrast, never `outline: none`)
- [ ] Touch targets are **≥ 44×44 CSS px** (WCAG 2.5.8)
- [ ] Respects **`prefers-reduced-motion`**
- [ ] Includes **`lang="en"`** on `<html>`
- [ ] Has an inline `<style>` block (self-contained, no external dependencies)
- [ ] Has an inline `<script>` block (no frameworks, no external CDN)
- [ ] Includes a **`<h1>`** describing what the component demonstrates
- [ ] Lists which WCAG SCs it satisfies in a comment block at the top

### File header comment template

```html
<!--
  Component: Accessible [Name]
  Pattern: [WAI-ARIA APG pattern name if applicable]
  WCAG: 2.1/2.2 Level AA
  Tests:
    ✅ Keyboard: [keys used]
    ✅ NVDA + Firefox: [date tested]
    ✅ VoiceOver + Safari: [date tested]
  SCs satisfied:
    - 1.3.1 Info and Relationships
    - 2.1.1 Keyboard
    - 2.4.3 Focus Order
    - 2.4.7 Focus Visible
    - 4.1.2 Name, Role, Value
    [add others]
-->
```

---

## Adding or improving a prompt

Prompts live in `prompts/` as Markdown files.

### Template structure

```markdown
# Prompt: [Descriptive title]

[One sentence: when to use this prompt]

---

## Prompt (copy & paste)

```
[The actual prompt text — what the user pastes into Claude]
```

---

## Tips

- [Tip 1]
- [Tip 2]
```

### Rules
- The prompt text should work when pasted directly into Claude with no additional context
- Reference relevant CSV databases at the bottom if useful
- Keep prompts focused — one primary use case per file

---

## Improving SKILL.md

`SKILL.md` is what Claude loads when the skill triggers. Keep it:

- **Under ~1500 lines** — Claude's context window is finite
- **Structured with numbered sections** — easier to reference in Notes for Claude
- **Code-heavy** — Claude learns better from examples than from rules
- **Cross-referenced** — point to CSV databases instead of duplicating data

When adding a new framework section:
1. Add it as `## N. Framework Name` (next available number)
2. Update the "Notes for Claude" bullet that lists stack examples
3. Update `README.md` to mention the new framework

---

## Commit conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add Vue 3 accessible modal example
fix: correct aria-expanded usage in accordion pattern
docs: update README file structure table
data: add 5 cognitive accessibility patterns to CSV
test: add pytest cases for --output json flag
chore: update .gitignore
```

Reference a WCAG SC in the commit body when fixing a specific criterion:

```
fix: correct focus trap in date picker dialog

Dialog was not trapping Tab correctly.
Fixes WCAG 2.1.2 (No Keyboard Trap).
```

---

## Pull request checklist

Before opening a PR, confirm:

- [ ] `pytest tests/ -v` passes with no errors
- [ ] `python scripts/search.py all --keyword [your topic]` returns expected results
- [ ] README updated if you added new files to `data/`, `prompts/`, `templates/`, or `examples/`
- [ ] CHANGELOG.md updated under `[Unreleased]`
- [ ] Commit message follows Conventional Commits format
- [ ] PR description references the relevant WCAG SC or WAI-ARIA pattern

---

## Code of conduct

This project follows the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

In short: be kind, be specific, and assume good intent. Accessibility is for everyone —
so is contributing to this project.

Questions? Open a [GitHub Discussion](https://github.com/mrKanoh/claude-wcag-accessibility-skill/discussions)
or ping [@mrKanoh](https://github.com/mrKanoh) in an Issue.
