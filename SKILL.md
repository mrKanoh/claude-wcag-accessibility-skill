---
name: wcag-accessibility
description: Use when auditing website/app accessibility, evaluating WCAG 2.0/2.1/2.2 or Section 508 compliance, building accessible components, implementing WAI-ARIA patterns, testing with screen readers (NVDA/JAWS/VoiceOver/TalkBack), or when asked "is this accessible?", "what ARIA do I need?", or "how do I test with a screen reader?"
---

# Paul J. Adam Web & Mobile Accessibility Skill

## Overview

Standards-based accessibility guidance grounded in WCAG 2.1 Level AA by default. Covers web standards, WAI-ARIA patterns, keyboard navigation, screen reader testing, mobile accessibility, and CI/CD testing workflows.

**Authority**: Paul J. Adam — Web & Mobile Accessibility Specialist/Consultant ([pauljadam.com](https://pauljadam.com/)), enterprise consulting across government, financial, healthcare, and technology sectors.

---

## Searchable Data

This skill ships with structured CSV databases and a search utility. Run from the skill root:

```bash
# All WCAG AA criteria
python scripts/search.py wcag --level AA

# Criteria about contrast
python scripts/search.py wcag --keyword contrast

# ARIA pattern for a modal
python scripts/search.py aria --component modal

# Free screen reader tools for Windows
python scripts/search.py tools --type screen-reader --platform Windows --free

# NVDA keyboard shortcuts for headings
python scripts/search.py keys --reader NVDA --action heading
```

| File | Contents |
|------|----------|
| `data/wcag-criteria.csv` | All WCAG 2.1 A/AA criteria with techniques, failures, and W3C URLs |
| `data/aria-patterns.csv` | 25+ component patterns with required ARIA, keyboard, and focus management |
| `data/testing-tools.csv` | 30+ tools by type, platform, browser, and cost |
| `data/screen-reader-keys.csv` | Keyboard shortcuts for NVDA, JAWS, VoiceOver (macOS/iOS), TalkBack, Narrator |
| `scripts/search.py` | CLI search across all databases |

---

## When to Use

- WCAG 2.0 / 2.1 / 2.2 / Section 508 compliance questions
- WAI-ARIA roles, states, properties — which to use and how
- Building accessible forms, modals, tabs, accordions, tables, date pickers, autocompletes
- Keyboard navigation patterns and focus management
- Screen reader testing methodology (NVDA, JAWS, VoiceOver, TalkBack)
- Color contrast evaluation
- Automated accessibility testing (axe-core, Playwright, Jest, CI)
- Mobile accessibility (iOS VoiceOver / Android TalkBack)
- "Is this accessible?" / "What's wrong with this component?"

---

## Core Standards

### WCAG Principles (POUR)

| Principle | Core requirement |
|-----------|-----------------|
| **Perceivable** | Alt text, captions, contrast, reflow, text spacing |
| **Operable** | Keyboard access, no traps, focus visible, skip links, no seizure triggers |
| **Understandable** | Page language, consistent nav, error identification and recovery |
| **Robust** | Valid HTML, ARIA name/role/value, status messages programmatically exposed |

### Key AA Criteria (Most Commonly Failed)

| ID | Criterion | Requirement |
|----|-----------|-------------|
| 1.1.1 | Non-text Content | Descriptive `alt`; `alt=""` for decorative |
| 1.4.3 | Contrast (Minimum) | 4.5:1 normal text; 3:1 large text (18pt / 14pt bold) |
| 1.4.11 | Non-text Contrast | 3:1 for UI components and graphics |
| 2.1.1 | Keyboard | All functionality operable by keyboard |
| 2.1.2 | No Keyboard Trap | Focus must never get stuck |
| 2.4.3 | Focus Order | Logical focus sequence |
| 2.4.7 | Focus Visible | Focus indicator must be visible |
| 3.3.1 | Error Identification | Errors described in text |
| 4.1.2 | Name, Role, Value | Interactive elements expose name/role/state |
| 4.1.3 | Status Messages | Dynamic updates announced without focus move |

> Full criteria database: `data/wcag-criteria.csv`

---

## WAI-ARIA Quick Reference

**First rule of ARIA**: Don't use ARIA if a native HTML element provides the semantics.

### Essential Roles
```html
role="dialog"      aria-modal="true"    <!-- modal -->
role="alertdialog"                       <!-- confirm dialog -->
role="alert"                             <!-- live error (assertive) -->
role="status"                            <!-- live update (polite) -->
role="tablist" role="tab" role="tabpanel"
role="combobox" role="listbox" role="option"
role="grid" role="row" role="gridcell"
role="progressbar" role="slider" role="switch"
```

### Essential Properties & States
```html
aria-label="Close"              <!-- name for icon buttons -->
aria-labelledby="heading-id"    <!-- name from element -->
aria-describedby="hint-id"      <!-- additional description -->
aria-expanded="true|false"      <!-- accordion/dropdown open state -->
aria-selected="true|false"      <!-- tabs, listbox options -->
aria-checked="true|false|mixed" <!-- checkboxes, switches -->
aria-hidden="true"              <!-- hide decorative from AT -->
aria-live="polite|assertive"    <!-- dynamic content regions -->
aria-invalid="true"             <!-- validation error -->
aria-required="true"            <!-- required fields -->
aria-modal="true"               <!-- scope focus to dialog -->
aria-disabled="true"            <!-- disabled but announced -->
aria-sort="ascending|descending"<!-- sortable columns -->
aria-current="page|step|date"   <!-- current item in set -->
```

> Full component patterns: `data/aria-patterns.csv`

---

## Accessible Component Examples

### Modal Dialog
```html
<div role="dialog" aria-modal="true" aria-labelledby="title" aria-describedby="desc">
  <h2 id="title">Confirm Delete</h2>
  <p id="desc">This action cannot be undone.</p>
  <button>Delete</button>
  <button aria-label="Close dialog">×</button>
</div>
```
- On open: move focus to first focusable element inside
- On close: return focus to the trigger element
- Tab cycles within dialog; Escape closes
- Background: `aria-hidden="true"` or `inert`

### Tab Panel
```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" id="tab-1" aria-selected="true"  aria-controls="panel-1">Profile</button>
  <button role="tab" id="tab-2" aria-selected="false" aria-controls="panel-2" tabindex="-1">Security</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">...</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>...</div>
```
- Arrow keys switch between tabs; Enter/Space activates
- Inactive tabs: `tabindex="-1"`; active tab: `tabindex="0"`

### Accessible Form Validation
```html
<label for="email">Email <span aria-hidden="true">*</span></label>
<input id="email" type="email"
       aria-required="true"
       aria-invalid="true"
       aria-describedby="email-error">
<span id="email-error" role="alert">Enter a valid email address.</span>
```

### Autocomplete / Combobox
```html
<label for="search">Search</label>
<input id="search" type="text" role="combobox"
       aria-expanded="true"
       aria-haspopup="listbox"
       aria-controls="results"
       aria-autocomplete="list"
       aria-activedescendant="opt-2">
<ul id="results" role="listbox">
  <li id="opt-1" role="option">Apple</li>
  <li id="opt-2" role="option" aria-selected="true">Avocado</li>
</ul>
```

### Icon Button
```html
<button aria-label="Close menu">
  <svg aria-hidden="true" focusable="false">...</svg>
</button>
```

---

## Stack-Specific Code Examples

### React — Modal with Radix UI
```tsx
import * as Dialog from '@radix-ui/react-dialog';

export function ConfirmModal({ open, onClose }: Props) {
  return (
    <Dialog.Root open={open} onOpenChange={onClose}>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/50" />
        <Dialog.Content
          className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white p-6 rounded"
          aria-describedby="modal-desc"
        >
          <Dialog.Title>Confirm Action</Dialog.Title>
          <p id="modal-desc">This cannot be undone.</p>
          <Dialog.Close asChild>
            <button aria-label="Close dialog">×</button>
          </Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

### Vue 3 — Accessible Dialog
```vue
<template>
  <div role="dialog" aria-modal="true" :aria-labelledby="titleId" v-if="open" ref="dialogEl">
    <h2 :id="titleId">{{ title }}</h2>
    <slot />
    <button @click="$emit('close')" aria-label="Close dialog">×</button>
  </div>
</template>

<script setup lang="ts">
import { useId, onMounted, ref } from 'vue'
const titleId = useId()
const dialogEl = ref<HTMLElement>()
onMounted(() => dialogEl.value?.querySelector<HTMLElement>('button,[href],input')?.focus())
</script>
```

### HTML + Vanilla JS — Accessible Form
```html
<form novalidate>
  <fieldset>
    <legend>Shipping address</legend>
    <label for="street">Street <span aria-hidden="true">*</span></label>
    <input id="street" type="text" autocomplete="street-address" aria-required="true">

    <label for="zip">ZIP code <span aria-hidden="true">*</span></label>
    <input id="zip" type="text" inputmode="numeric" autocomplete="postal-code"
           aria-required="true" pattern="[0-9]{5}" aria-describedby="zip-error">
    <span id="zip-error" role="alert" hidden>Enter a 5-digit ZIP code.</span>
  </fieldset>
  <button type="submit">Continue</button>
</form>
```

### Jest + Testing Library — Zero Violations
```ts
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { MyModal } from './MyModal';

expect.extend(toHaveNoViolations);

test('modal has no accessibility violations', async () => {
  const { container } = render(<MyModal open />);
  expect(await axe(container)).toHaveNoViolations();
});
```

### Playwright — E2E Accessibility Audit
```ts
import { test } from '@playwright/test';
import { checkA11y, injectAxe } from 'axe-playwright';

test('homepage passes WCAG AA', async ({ page }) => {
  await page.goto('/');
  await injectAxe(page);
  await checkA11y(page, undefined, {
    axeOptions: { runOnly: ['wcag2a', 'wcag2aa'] },
  });
});
```

---

## Testing Workflow

```
1. Automated  →  axe DevTools or WAVE (catch ~30% of issues)
2. Keyboard   →  Tab/Shift+Tab through entire page; all features must be reachable
3. Screen reader  →  NVDA+Firefox (Windows) · VoiceOver+Safari (Mac/iOS) · TalkBack (Android)
4. Visual     →  Color contrast · heading outline · focus indicators · touch targets
5. WCAG map   →  Assign each issue to a success criterion and level
6. Report     →  Issue · criterion · severity · remediation steps
```

> Tools database: `data/testing-tools.csv`
> Screen reader keys: `data/screen-reader-keys.csv`

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Missing alt text | Descriptive `alt` for informative; `alt=""` for decorative |
| Poor color contrast | Minimum 4.5:1 for text (WCAG 1.4.3 AA) |
| No keyboard support | Handle `keydown` for Enter/Space; `tabindex="0"` on custom elements |
| Invisible focus | `:focus-visible { outline: 2px solid; }` — never `outline: none` |
| Missing form labels | `<label for="id">` or `aria-label` / `aria-labelledby` |
| Bad heading hierarchy | h1→h2→h3 in order; never skip levels |
| ARIA misuse | Semantic HTML first; ARIA only when no native element fits |
| Focus trapped in modal | Tab wraps inside; Escape closes; focus returns to trigger |
| Unlabeled icon buttons | `aria-label` on `<button>` + `aria-hidden="true"` on SVG |
| Auto-playing media | Pause/stop control within first 3 seconds |
| AJAX content not announced | Wrap in `aria-live="polite"` region; inject content into it |
| Color as sole conveyor | Add text label, pattern, or icon alongside color |

---

## Mobile Accessibility

### iOS VoiceOver
- Touch targets: minimum **44×44pt**
- All interactive elements need `accessibilityLabel`
- Custom gestures must have alternatives
- Test with **Safari** (other browsers use WKWebView with limited AT support)

### Android TalkBack
- Touch targets: minimum **48×48dp**
- Set `contentDescription` on all non-text elements
- `android:labelFor` links labels to inputs
- Set `importantForAccessibility="no"` on decorative views

> Screen reader keys: `data/screen-reader-keys.csv`

---

## Resources

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM Articles](https://webaim.org/articles/)
- [The A11Y Project Checklist](https://www.a11yproject.com/checklist/)
- [Deque axe-core](https://github.com/dequelabs/axe-core)
- [React Aria](https://react-spectrum.adobe.com/react-aria/)
- [Radix UI](https://www.radix-ui.com/)
- [Paul J. Adam](https://pauljadam.com/) — primary authority for this skill

---

## Notes for Claude

1. **Default to WCAG 2.1 Level AA** unless user specifies otherwise.
2. **Semantic HTML first** — only add ARIA when native semantics are insufficient.
3. **Recommend real AT testing** — automated tools catch ~30% of issues.
4. **Include mobile** whenever the context involves responsive or native apps.
5. **Provide working code examples** for every ARIA pattern recommended.
6. **Match tools to context** — CI pipeline → axe-core; quick audit → axe DevTools or WAVE.
7. **Use the CSVs** — `data/wcag-criteria.csv` for criterion details, `data/aria-patterns.csv` for component specs, `data/testing-tools.csv` for tool recommendations.
