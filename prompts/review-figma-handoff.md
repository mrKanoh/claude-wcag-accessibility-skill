# Prompt: Review a Figma / design handoff for accessibility

Use when a designer hands off specs to dev and you want a structured a11y review.

---

## Prompt (copy & paste)

```
Review the following design handoff for accessibility gaps before development begins.

Evaluate each category and flag what is missing or unclear:

1. SEMANTIC STRUCTURE
   - Are heading levels (H1-H6) annotated?
   - Are landmark regions (header, nav, main, footer) marked?
   - Are lists, tables, or form groups identified?

2. FOCUS ORDER
   - Is the tab order numbered/annotated on interactive elements?
   - Does the order match visual reading order?

3. KEYBOARD INTERACTIONS
   - Are keyboard behaviors specified for custom components (e.g. tabs, dropdowns, modals)?
   - Is Esc / Enter / Space / Arrow key behavior documented?

4. ARIA ANNOTATIONS
   - Does each custom component have its role, accessible name, and state documented?
   - Are icon-only buttons given accessible names?

5. COMPONENT STATES
   - Are all interactive states shown: default, hover, focus, active, disabled, error, selected?
   - Is the focus ring visible and contrast-checked?

6. COLOR & CONTRAST
   - Are contrast ratios documented for text and UI components?
   - Is color used alone to convey meaning anywhere?

7. TOUCH & TARGET SIZE
   - Are targets ≥ 24×24 CSS px (WCAG 2.5.8)? Preferably ≥ 44×44?
   - Is spacing between small targets sufficient?

8. MOTION & ANIMATION
   - Is a prefers-reduced-motion alternative specified for animations?

9. ERRORS & STATUS
   - Are error messages inline (not just color-coded)?
   - Is there an aria-live / role=alert region for dynamic feedback?

Design handoff description / screenshots / specs:
[PASTE or describe the design spec here]
```
