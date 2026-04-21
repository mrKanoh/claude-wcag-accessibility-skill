---
name: Bug report
about: Report incorrect WCAG data, broken keyboard behavior, or wrong ARIA patterns
title: "[BUG] "
labels: bug
assignees: ''
---

## What's wrong?

<!-- Describe the issue clearly. Is it in a CSV, in SKILL.md, in a prompt, in an example component? -->

## Where is it?

- [ ] `data/*.csv` — incorrect WCAG/ARIA/legal data
- [ ] `SKILL.md` — wrong guidance or code example
- [ ] `prompts/*.md` — prompt produces incorrect output
- [ ] `examples/components/*.html` — keyboard or screen reader behavior broken
- [ ] `scripts/search.py` — search returns wrong results
- [ ] `templates/` — template has errors
- [ ] `README.md` / `RESOURCES.md` — documentation incorrect

**File**: `[e.g. data/aria-patterns.csv]`
**Line / field**: `[e.g. row for "Modal", column "keyboard"]`

## What's incorrect?

<!-- Current (wrong) value: -->
<!-- Expected (correct) value: -->
<!-- Reference (WCAG SC, WAI-ARIA APG URL, or MDN link): -->

## Steps to reproduce (for code/component bugs)

1. Open `examples/components/[file].html` in a browser
2. Use keyboard / screen reader: [describe steps]
3. Observe: [what goes wrong]
4. Expected: [what should happen]

## Environment (for component bugs)

- OS: [e.g. Windows 11, macOS Sonoma]
- Browser: [e.g. Firefox 124, Chrome 123]
- Screen reader: [e.g. NVDA 2023.3, VoiceOver macOS 14.4]

## Additional context

<!-- Any links, screenshots, or recordings that help explain the issue -->
