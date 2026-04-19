# Prompt: Convert WCAG SC to Acceptance Criteria

Use when writing user stories for a sprint — turn WCAG success criteria into dev-ready AC.

---

## Prompt (copy & paste)

```
Convert the following WCAG Success Criteria into developer-ready Acceptance Criteria for a user story.

For each criterion, write:
- One "Given / When / Then" test scenario (Gherkin style)
- A plain-language AC bullet (for the story card)
- The automated test hint (jest-axe / Playwright / manual)

WCAG Success Criteria to convert:
[LIST SCs — e.g. "1.4.3 Contrast (Minimum) AA", "2.1.1 Keyboard A", "4.1.2 Name Role Value A"]

Component / feature context:
[DESCRIBE the feature — e.g. "Login form with email, password, and submit button"]
```

---

## Example output format

> **1.4.3 Contrast (Minimum) — AA**
>
> **AC**: All body text and interactive labels must have a contrast ratio of at least 4.5:1 against their background.
>
> **Gherkin**:
> ```
> Given a user views the login form
> When they inspect the email label and input text
> Then the contrast ratio between text and background is ≥ 4.5:1
> ```
>
> **Automated**: Colour Contrast Analyser (manual spot-check) + axe-core (automated in CI).
