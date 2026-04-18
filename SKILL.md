---
name: wcag-accessibility
description: Use when auditing website/app accessibility, evaluating WCAG 2.0/2.1/2.2 or Section 508 compliance, building accessible components (forms, modals, tabs, tables), implementing WAI-ARIA roles/states/properties, testing with screen readers (NVDA, JAWS, VoiceOver, TalkBack), or asking "is this accessible?" about any web or mobile UI.
---

# Paul J. Adam Web & Mobile Accessibility Skill

## Overview

Comprehensive accessibility guidance grounded in WCAG 2.1 Level AA by default. Covers web standards, WAI-ARIA, keyboard navigation, screen reader testing, mobile accessibility (iOS/Android), and automated + manual testing workflows.

**Authority**: Paul J. Adam — Web & Mobile Accessibility Specialist/Consultant (pauljadam.com), enterprise-level consulting across government, financial, healthcare, and technology sectors.

---

## When to Use

### Accessibility Audits & Testing
- Evaluating website/app accessibility compliance
- WCAG 2.0, 2.1, 2.2, or Section 508 questions
- Choosing or configuring accessibility testing tools
- "Is this accessible?" or "How do I test for accessibility?"

### Design & Development
- Building accessible forms, buttons, menus, dialogs, or data tables
- WAI-ARIA roles, states, and properties questions
- Accessible component patterns (tabs, accordions, date pickers, drag-and-drop)
- Mobile app accessibility (iOS VoiceOver / Android TalkBack)

### Standards & Guidelines
- WCAG success criteria and techniques
- Accessibility checklists or reporting templates
- Keyboard navigation, color contrast, or screen reader compatibility

### When NOT to Use
- General HTML/CSS questions with no accessibility angle
- Performance, SEO, or non-accessibility design tasks

---

## Core Knowledge

### 1. WCAG Principles (POUR)

| Principle | Meaning |
|-----------|---------|
| **Perceivable** | Content must be presentable in ways users can perceive (alt text, captions, contrast) |
| **Operable** | UI must be navigable by keyboard and not cause seizures |
| **Understandable** | Content and operation must be understandable |
| **Robust** | Content must work with current and future assistive technologies |

**Conformance levels**: A (minimum) → AA (standard target) → AAA (enhanced)

---

### 2. Key WCAG Success Criteria

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 1.1.1 Non-text Content | A | Descriptive alt text for informative images; `alt=""` for decorative |
| 1.4.3 Contrast (Minimum) | AA | 4.5:1 normal text, 3:1 large text |
| 1.4.11 Non-text Contrast | AA | 3:1 for UI components and graphical objects |
| 2.1.1 Keyboard | A | All functionality available via keyboard |
| 2.1.2 No Keyboard Trap | A | Focus must never be trapped |
| 2.4.1 Bypass Blocks | A | Skip navigation links |
| 2.4.3 Focus Order | A | Logical focus sequence |
| 4.1.2 Name, Role, Value | A | Interactive elements must expose name, role, and state |

---

### 3. WAI-ARIA Quick Reference

**Essential roles**
```html
role="dialog"        <!-- modal dialogs -->
role="alertdialog"   <!-- urgent alerts requiring response -->
role="alert"         <!-- live error regions (aria-live="assertive") -->
role="tablist/tab/tabpanel"
role="grid"          <!-- interactive data grids -->
role="listbox/option"
role="combobox"      <!-- autocomplete/select -->
```

**Essential states & properties**
```html
aria-label="Close dialog"          <!-- accessible name for icon buttons -->
aria-labelledby="heading-id"       <!-- name from existing element -->
aria-describedby="hint-id"         <!-- additional description -->
aria-expanded="true|false"         <!-- accordion/dropdown state -->
aria-selected="true|false"         <!-- tabs, listbox options -->
aria-checked="true|false|mixed"    <!-- checkboxes, toggles -->
aria-hidden="true"                 <!-- hide from AT (decorative/duplicate) -->
aria-live="polite|assertive"       <!-- dynamic content announcements -->
aria-invalid="true"                <!-- form validation errors -->
aria-required="true"               <!-- required fields -->
aria-modal="true"                  <!-- scopes focus to dialog -->
aria-sort="ascending|descending"   <!-- sortable table columns -->
```

**First rule of ARIA**: Don't use ARIA if a native HTML element provides the semantics.

---

### 4. Accessible Component Patterns

#### Modal Dialog
```html
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">Confirm Action</h2>
  <p id="modal-desc">This cannot be undone.</p>
  <!-- Focus trapped inside; Escape closes; focus returns to trigger -->
  <button>Confirm</button>
  <button aria-label="Close dialog">×</button>
</div>
```

#### Tab Panel
```html
<div role="tablist" aria-label="Settings sections">
  <button role="tab" aria-selected="true"  aria-controls="panel-1" id="tab-1">General</button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2">Privacy</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">...</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>...</div>
<!-- Arrow keys switch tabs; Enter/Space activates -->
```

#### Accordion
```html
<button aria-expanded="false" aria-controls="section-1">Section Title</button>
<div id="section-1" hidden>Content here</div>
```

#### Form Validation
```html
<label for="email">Email <span aria-hidden="true">*</span></label>
<input id="email" type="email" aria-required="true"
       aria-invalid="true" aria-describedby="email-error">
<span id="email-error" role="alert">Enter a valid email address.</span>
```

#### Icon Button
```html
<button aria-label="Close menu">
  <svg aria-hidden="true" focusable="false">...</svg>
</button>
```

---

### 5. Keyboard Interaction Patterns

| Element | Keys |
|---------|------|
| Links, buttons | Tab/Shift+Tab to focus; Enter to activate |
| Buttons | Space also activates |
| Tabs | Arrow keys between tabs; Enter/Space activates |
| Accordion | Enter/Space toggles; Tab moves between triggers |
| Dialog | Tab cycles within; Escape closes |
| Select/Listbox | Arrow keys navigate options; Enter selects |
| Grid/Table | Arrow keys navigate cells |
| Date picker | Arrow keys navigate calendar |

---

### 6. Color Contrast

| Standard | Normal text | Large text (18pt / 14pt bold) |
|----------|-------------|-------------------------------|
| WCAG AA  | 4.5:1       | 3:1                           |
| WCAG AAA | 7:1         | 4.5:1                         |

- Color must never be the **sole** means of conveying information.
- UI components and graphical objects: 3:1 minimum (WCAG 1.4.11).

**Tools**: Colour Contrast Analyser (desktop), Chrome DevTools contrast checker, WebAIM Contrast Checker.

---

### 7. Testing Tools

#### Browser Extensions
| Tool | Browser | Best for |
|------|---------|---------|
| **axe DevTools** (Deque) | Chrome, Firefox, Edge | Automated rule checking |
| **WAVE** | Chrome, Firefox | Visual overlay of issues |
| **Accessibility Insights** | Edge, Chrome | Guided manual checks |
| **ARC Toolkit** | Chrome | WCAG-mapped findings |

#### Command Line / CI
```bash
# axe-core CLI
npm install -g @axe-core/cli
axe https://example.com

# axe-core in tests (Jest + Testing Library)
import { axe, toHaveNoViolations } from 'jest-axe';
expect(await axe(container)).toHaveNoViolations();
```

#### Screen Readers
| Reader | Platform | Pairing |
|--------|----------|---------|
| **NVDA** (free) | Windows | Firefox or Chrome |
| **JAWS** | Windows | Chrome or Edge |
| **VoiceOver** | macOS / iOS | Safari |
| **TalkBack** | Android | Chrome |

#### Mobile Tools
- **Accessibility Inspector** (Xcode) — iOS
- **Google Accessibility Scanner** — Android
- **a11yTools** — iOS app for auditing

---

### 8. Screen Reader Testing Essentials

**NVDA quick keys** (browse mode)
| Key | Action |
|-----|--------|
| H / Shift+H | Next/prev heading |
| F | Next form field |
| T | Next table |
| B | Next button |
| L | Next list |
| Insert+F7 | Elements list |

**VoiceOver (macOS)** — VO = Control+Option
| Keys | Action |
|------|--------|
| VO+Right/Left | Read next/prev element |
| VO+U | Rotor (headings, links, etc.) |
| VO+Space | Activate element |
| VO+Shift+M | Context menu |

**VoiceOver (iOS)**
- Swipe right/left to navigate
- Double-tap to activate
- Three-finger swipe to scroll
- Rotor: two-finger rotation

---

### 9. Mobile Accessibility

**Touch targets**: minimum 48×48 dp (Android) / 44×44 pt (iOS).

**iOS VoiceOver checklist**
- [ ] All interactive elements have meaningful labels
- [ ] Custom gestures have alternatives
- [ ] Accessibility traits set correctly (button, header, link, image)
- [ ] `accessibilityLabel`, `accessibilityHint` set where needed

**Android TalkBack checklist**
- [ ] `contentDescription` on all non-text elements
- [ ] `importantForAccessibility` set appropriately
- [ ] Touch targets ≥ 48dp
- [ ] Custom views implement `AccessibilityNodeInfoCompat`

---

### 10. Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Missing alt text | Descriptive `alt` for informative; `alt=""` for decorative |
| Poor color contrast | Minimum 4.5:1 for text (WCAG AA) |
| No keyboard support | Handle `keydown` Enter/Space; add `tabindex="0"` if needed |
| Invisible focus indicator | Add visible `:focus-visible` outline; never `outline: none` |
| Missing form labels | `<label for="id">` or `aria-label` / `aria-labelledby` |
| Broken heading hierarchy | Use h1→h2→h3 in order; never skip levels |
| ARIA misuse | Use semantic HTML first; ARIA only when no native element exists |
| Focus trapped in modal | Tab must cycle within modal; Escape must close it |
| Unlabeled icon buttons | Add `aria-label` or visible text |
| Auto-playing media | Provide pause/stop control within first 3 seconds |
| AJAX content not announced | Wrap updates in `aria-live="polite"` region |

---

## Recommended Audit Workflow

1. **Automated scan** — Run axe DevTools or WAVE; fix all violations.
2. **Keyboard-only navigation** — Tab through entire page; verify all features reachable and operable.
3. **Screen reader testing** — NVDA+Firefox (Windows), VoiceOver+Safari (Mac/iOS), TalkBack (Android).
4. **Visual checks** — Color contrast, heading structure, focus indicators, touch targets.
5. **WCAG mapping** — Map findings to specific success criteria and levels.
6. **Report** — Document issue, criterion, severity, and remediation steps.

---

## Design Systems with Built-in Accessibility

- **React Aria** (Adobe) — Headless, fully accessible hooks
- **Radix UI** — Unstyled, accessible primitives
- **Headless UI** — For Tailwind CSS projects
- **Adobe Spectrum** — Adobe's accessible design system
- **U.S. Web Design System (USWDS)** — Federal government standard

---

## Key Resources

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM Articles](https://webaim.org/articles/)
- [The A11Y Project Checklist](https://www.a11yproject.com/checklist/)
- [Paul J. Adam's Site](https://pauljadam.com/)
- [axe-core GitHub](https://github.com/dequelabs/axe-core)

---

## Notes for Claude

1. **Default to WCAG 2.1 Level AA** unless the user requests otherwise.
2. **Prefer semantic HTML** over ARIA — only add ARIA when native semantics are insufficient.
3. **Always recommend manual testing** alongside automated tools — automated tools catch ~30% of issues.
4. **Include mobile** when context involves responsive or native app development.
5. **Provide code examples** for every ARIA pattern recommendation.
6. **Be specific about tools** — match recommendations to the user's tech stack and environment (CI, browser, OS).
