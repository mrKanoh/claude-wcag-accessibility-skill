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

# Semantic HTML reference
python scripts/search.py semantic --element nav

# Accessible typography rules by category
python scripts/search.py typography --category Spacing

# Color palette rules
python scripts/search.py color --scope Non-text

# Accessibility KPIs
python scripts/search.py kpis --category Remediation

# Handoff checklist by phase / owner
python scripts/search.py handoff --phase Design --owner Designer

# Models of disability
python scripts/search.py models --keyword social
```

| File | Contents |
|------|----------|
| `data/wcag-criteria.csv` | WCAG 2.1 A/AA + **WCAG 2.2** (2.4.11–2.4.13, 2.5.7–2.5.8, 3.2.6, 3.3.7–3.3.9) |
| `data/aria-patterns.csv` | 25+ component patterns · ARIA · keyboard · focus mgmt |
| `data/testing-tools.csv` | 30+ tools by type · platform · browser · cost |
| `data/screen-reader-keys.csv` | Shortcuts for NVDA · JAWS · VoiceOver (macOS/iOS) · TalkBack · Narrator |
| `data/semantic-html.csv` | Semantic HTML element → role → when to use / avoid |
| `data/typography-rules.csv` | 20 accessible typography rules mapped to WCAG |
| `data/color-palette-rules.csv` | Palette design rules (contrast, color-blindness, HCM, states) |
| `data/kpis.csv` | 15 accessibility KPIs with formulas, targets, cadence |
| `data/handoff-checklist.csv` | Research → Design → Dev → QA → Release handoff |
| `data/disability-models.csv` | Medical / Social / Biopsychosocial / CRPD / Identity |
| `data/glossary-es.csv` | Spanish ↔ English a11y glossary (70+ terms with definitions) |
| `data/legal-framework.csv` | 25+ jurisdictions: ADA, EAA, Section 508, AODA, LGPD, and more |
| `scripts/search.py` | CLI search across all 12 databases |
| `templates/audit-report.md` | Fill-in audit report template |
| `templates/a11y-ci.yml` | GitHub Actions pipeline (axe + pa11y + Playwright + Lighthouse) |
| `prompts/audit-component.md` | Prompt: audit a UI component |
| `prompts/sc-to-acceptance-criteria.md` | Prompt: WCAG SC → Gherkin ACs |
| `prompts/generate-alt-text.md` | Prompt: generate alt text |
| `prompts/review-figma-handoff.md` | Prompt: review design handoff |
| `prompts/summarize-audit-findings.md` | Prompt: exec summary from findings |
| `prompts/generate-aria-pattern.md` | Prompt: generate any accessible widget |

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
| **Standards** | WCAG 2.0 / 2.1 / **2.2**, Section 508, EN 301 549, EAA, WAI-ARIA 1.2 |
| **Semantic HTML** | Landmarks, headings, lists, tables, forms — full element reference |
| **Typography** | Size, spacing, reflow, zoom, dyslexia-friendly faces |
| **Color palettes** | Contrast matrix, state tokens, dark mode, forced-colors, color blindness |
| **Audit** | Scope, sampling, severity scale, ACR/VPAT, remediation roadmap |
| **Inclusive research** | Recruitment, consent, modality, disability categories |
| **Handoff** | Designer → Developer → QA phase-by-phase checklist |
| **KPIs** | Automated violation density, MTTR, conformance rate, AC coverage |
| **Disability theory** | Medical / Social / ICF / CRPD / Identity models |
| **Stacks** | Next.js App Router, Angular, Svelte, Astro, SolidJS + SwiftUI, Jetpack Compose |
| **User preferences** | prefers-reduced-motion, prefers-contrast, forced-colors, prefers-reduced-transparency |
| **Alternative input** | Switch access, voice control, eye tracking, head pointer, cognitive a11y (COGA) |
| **Legal** | 25+ jurisdictions with law, standard, scope, and effective date |
| **ES glossary** | Spanish ↔ English (70+ terms with definitions and context) |
| **Templates** | Audit report template, GitHub Actions CI pipeline |
| **Prompts** | 6 Claude prompts ready to copy-paste |
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
    wcag-criteria.csv         ← WCAG 2.1 A/AA + WCAG 2.2 additions
    aria-patterns.csv         ← Component ARIA patterns
    testing-tools.csv         ← Accessibility testing tools
    screen-reader-keys.csv    ← Shortcuts for 5 screen readers
    semantic-html.csv         ← Semantic HTML reference
    typography-rules.csv      ← Accessible typography rules
    color-palette-rules.csv   ← Palette design rules (AA, HCM, CVD)
    kpis.csv                  ← Accessibility KPIs
    handoff-checklist.csv     ← Design → Dev → QA handoff
    disability-models.csv     ← Theoretical models of disability
    glossary-es.csv           ← Spanish ↔ English glossary
    legal-framework.csv       ← Legal frameworks by jurisdiction
  scripts/
    search.py                 ← CLI search across all 12 databases
  templates/
    audit-report.md           ← Fill-in audit report template
    a11y-ci.yml               ← GitHub Actions CI pipeline
  prompts/
    audit-component.md
    sc-to-acceptance-criteria.md
    generate-alt-text.md
    review-figma-handoff.md
    summarize-audit-findings.md
    generate-aria-pattern.md
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
- More stack examples (Svelte, Angular, Next.js App Router, SwiftUI, Jetpack Compose)
- Additional ARIA patterns (virtual lists, carousels, complex data grids)
- Localization of Spanish-language a11y terminology
- Remediation cost/effort estimation heuristics

---

## License

MIT — free to use, share, and adapt with attribution.
