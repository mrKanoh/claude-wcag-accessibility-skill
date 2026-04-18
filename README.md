# wcag-accessibility

> A Claude Code skill for web and mobile accessibility — grounded in WCAG 2.1 Level AA and Paul J. Adam's expertise.

---

## What This Skill Does

This skill gives Claude comprehensive, actionable knowledge to help you:

- **Audit** websites and apps against WCAG 2.0 / 2.1 / 2.2 and Section 508
- **Build** accessible components: forms, modals, tabs, accordions, data tables, date pickers, autocompletes
- **Implement** WAI-ARIA roles, states, and properties correctly
- **Test** with real assistive technologies: NVDA, JAWS, VoiceOver, TalkBack
- **Set up** automated accessibility testing in CI/CD (axe-core, Playwright, Jest)
- **Evaluate** color contrast, keyboard navigation, focus management, and mobile touch targets

Comes with **searchable CSV databases** and a **Python search utility** — inspired by the `ui-ux-pro-max` skill architecture.

---

## Installation

### Claude Code (CLI / Desktop)

Clone directly into your personal skills directory:

```bash
# macOS / Linux
git clone https://github.com/mrKanoh/wcag-accessibility-skill.git ~/.claude/skills/wcag-accessibility

# Windows (PowerShell)
git clone https://github.com/mrKanoh/wcag-accessibility-skill.git "$env:USERPROFILE\.claude\skills\wcag-accessibility"
```

Or copy just the `SKILL.md`:

```bash
# macOS / Linux
mkdir -p ~/.claude/skills/wcag-accessibility
curl -o ~/.claude/skills/wcag-accessibility/SKILL.md \
  https://raw.githubusercontent.com/mrKanoh/wcag-accessibility-skill/main/SKILL.md
```

Claude Code automatically discovers skills in `~/.claude/skills/`. No restart required.

---

## Searchable Databases

Run searches from the skill root:

```bash
# All WCAG AA criteria
python scripts/search.py wcag --level AA

# Criteria about contrast
python scripts/search.py wcag --keyword contrast --url

# Full ARIA spec for a modal dialog
python scripts/search.py aria --component modal --detail

# ARIA patterns involving keyboard focus
python scripts/search.py aria --keyword focus

# Free screen reader tools for Windows
python scripts/search.py tools --type screen-reader --platform Windows --free --url

# All browser extensions
python scripts/search.py tools --type browser-extension

# NVDA shortcuts for heading navigation
python scripts/search.py keys --reader NVDA --action heading

# All VoiceOver shortcuts on macOS
python scripts/search.py keys --reader VoiceOver --platform macOS
```

| File | Rows | Contents |
|------|------|----------|
| `data/wcag-criteria.csv` | 46 | All WCAG 2.1 A/AA criteria · techniques · failures · W3C URLs |
| `data/aria-patterns.csv` | 25+ | Component patterns · required ARIA · keyboard · focus management |
| `data/testing-tools.csv` | 30+ | Tools by type · platform · browser · cost |
| `data/screen-reader-keys.csv` | 80+ | Shortcuts for NVDA · JAWS · VoiceOver (macOS/iOS) · TalkBack · Narrator |
| `scripts/search.py` | — | CLI search tool across all databases |

---

## Trigger Examples

Claude loads this skill automatically when you ask things like:

- *"Is this button accessible?"*
- *"What's the correct ARIA pattern for a modal dialog?"*
- *"How do I test my site with NVDA?"*
- *"Does this color combination pass WCAG AA contrast?"*
- *"How do I make this form validation accessible?"*
- *"What keyboard shortcuts does VoiceOver use?"*
- *"Set up axe-core in my Playwright tests"*
- *"My React tab component isn't announcing correctly in JAWS"*
- *"What WCAG criterion covers focus visibility?"*

---

## Skill Coverage

| Domain | Topics |
|--------|--------|
| **Standards** | WCAG 2.0 / 2.1 / 2.2, Section 508, WAI-ARIA 1.1 |
| **Components** | Modals, tabs, accordions, forms, tables, date pickers, autocomplete, icon buttons, carousels, sliders, drag-and-drop |
| **Keyboard** | Tab order, focus management, arrow key patterns, keyboard traps |
| **Color** | Contrast ratios AA/AAA, non-text contrast, color-only information |
| **Screen readers** | NVDA, JAWS, VoiceOver (macOS + iOS), TalkBack (Android), Narrator |
| **Mobile** | Touch targets, gesture alternatives, VoiceOver/TalkBack checklists |
| **Testing tools** | axe DevTools, WAVE, Accessibility Insights, ARC Toolkit, axe-core CLI |
| **CI/CD** | axe-core + Jest/Testing Library, Playwright + axe, GitHub Actions |
| **Stacks** | React (Radix UI), Vue 3, HTML+Vanilla JS, Playwright, Jest |
| **Design systems** | React Aria, Radix UI, Headless UI, USWDS, Adobe Spectrum |

---

## File Structure

```
wcag-accessibility/
  SKILL.md                    ← Claude skill (loaded by Claude Code)
  README.md                   ← This file
  data/
    wcag-criteria.csv         ← All WCAG 2.1 A/AA criteria
    aria-patterns.csv         ← 25+ component ARIA patterns
    testing-tools.csv         ← 30+ accessibility testing tools
    screen-reader-keys.csv    ← Keyboard shortcuts for 5 screen readers
  scripts/
    search.py                 ← CLI search utility
```

---

## Attribution & Credits

This skill is based on the work and expertise of **Paul J. Adam**, Web & Mobile Accessibility Specialist/Consultant based in Austin, TX.

Paul provides enterprise-level accessibility consulting across government, financial, healthcare, and technology sectors, and has been a leading voice in the web accessibility community for over a decade.

- **Website**: [pauljadam.com](https://pauljadam.com/)
- **Specialty**: WCAG compliance, WAI-ARIA, iOS/Android accessibility, screen reader testing

Additional standards and references:
- [W3C Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM](https://webaim.org/)
- [Deque axe-core](https://github.com/dequelabs/axe-core)
- [The A11Y Project](https://www.a11yproject.com/)

---

## Contributing

Improvements, corrections, and new component patterns are welcome. Open a PR referencing the relevant WCAG success criterion or WAI-ARIA pattern.

Areas that could grow:
- More stack examples (Svelte, Angular, Next.js App Router)
- Additional ARIA patterns (data grids, tree views, virtual lists)
- WCAG 2.2 new criteria (2.4.11–2.4.13, 3.2.6, 3.3.7–3.3.8)
- Automated test templates per framework

---

## License

MIT — free to use, share, and adapt with attribution.
