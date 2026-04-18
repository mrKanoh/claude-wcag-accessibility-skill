# wcag-accessibility

> A Claude Code skill for web and mobile accessibility — grounded in WCAG 2.1 Level AA and Paul J. Adam's expertise.

---

## What This Skill Does

This skill gives Claude comprehensive, actionable knowledge to help you:

- **Audit** websites and apps against WCAG 2.0 / 2.1 / 2.2 and Section 508
- **Build** accessible components: forms, modals, tabs, accordions, data tables, date pickers, autocompletes
- **Implement** WAI-ARIA roles, states, and properties correctly
- **Test** with real assistive technologies: NVDA, JAWS, VoiceOver, TalkBack
- **Set up** automated accessibility testing in CI/CD pipelines
- **Evaluate** color contrast, keyboard navigation, focus management, and mobile touch targets

---

## Installation

### Claude Code (CLI / Desktop)

Copy `SKILL.md` into your personal skills directory:

```bash
# macOS / Linux
cp SKILL.md ~/.claude/skills/wcag-accessibility/SKILL.md

# Windows (PowerShell)
Copy-Item SKILL.md "$env:USERPROFILE\.claude\skills\wcag-accessibility\SKILL.md" -Force
```

Or clone the repo directly:

```bash
# macOS / Linux
git clone https://github.com/mrKanoh/wcag-accessibility-skill.git ~/.claude/skills/wcag-accessibility

# Windows (PowerShell)
git clone https://github.com/mrKanoh/wcag-accessibility-skill.git "$env:USERPROFILE\.claude\skills\wcag-accessibility"
```

Claude Code automatically discovers skills in `~/.claude/skills/`. No restart required.

---

## Trigger Examples

Claude will load this skill automatically when you ask things like:

- *"Is this button accessible?"*
- *"What's the correct ARIA pattern for a modal dialog?"*
- *"How do I test my site with a screen reader?"*
- *"Does this color combination pass WCAG AA contrast?"*
- *"How do I make this form validation accessible?"*
- *"What keyboard shortcuts does VoiceOver use?"*
- *"Set up axe-core in my Jest tests"*
- *"My React tab component isn't announcing correctly in NVDA"*

---

## Skill Coverage

| Domain | Topics |
|--------|--------|
| **Standards** | WCAG 2.0 / 2.1 / 2.2, Section 508, WAI-ARIA 1.1 |
| **Components** | Modals, tabs, accordions, forms, tables, date pickers, autocomplete, icon buttons |
| **Keyboard** | Tab order, focus management, arrow key patterns, keyboard traps |
| **Color** | Contrast ratios (AA/AAA), non-text contrast, color-only information |
| **Screen readers** | NVDA, JAWS, VoiceOver (macOS + iOS), TalkBack (Android) |
| **Mobile** | Touch targets, gesture alternatives, VoiceOver/TalkBack checklists |
| **Testing tools** | axe DevTools, WAVE, Accessibility Insights, ARC Toolkit, axe-core CLI |
| **CI/CD** | axe-core + Jest/Testing Library integration |
| **Design systems** | React Aria, Radix UI, Headless UI, USWDS, Adobe Spectrum |

---

## File Structure

```
wcag-accessibility/
  SKILL.md    ← Claude skill (frontmatter + full reference)
  README.md   ← This file (for GitHub)
```

---

## Attribution & Credits

This skill is based on the work and expertise of **Paul J. Adam**, Web & Mobile Accessibility Specialist/Consultant based in Austin, TX.

Paul provides enterprise-level accessibility consulting across government, financial, healthcare, and technology sectors, and has been a leading voice in the web accessibility community for over a decade.

- **Website**: [pauljadam.com](https://pauljadam.com/)
- **Specialty**: WCAG compliance, WAI-ARIA, iOS/Android accessibility, screen reader testing

Additional standards and references:
- [W3C Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM](https://webaim.org/)
- [Deque axe-core](https://github.com/dequelabs/axe-core)
- [The A11Y Project](https://www.a11yproject.com/)

---

## Contributing

Improvements, corrections, and new component patterns are welcome. Open a PR or issue referencing the relevant WCAG success criterion or WAI-ARIA pattern.

---

## License

MIT — free to use, share, and adapt with attribution.
