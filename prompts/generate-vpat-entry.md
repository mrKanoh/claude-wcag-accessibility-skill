# Prompt: Generate VPAT entry from audit findings

Use when you have a set of audit findings and need to translate them into
Accessibility Conformance Report (ACR / VPAT) language.

---

## Prompt (copy & paste)

```
You are an accessibility conformance specialist. Given the following audit findings,
generate the corresponding VPAT 2.5 entries.

For each WCAG Success Criterion affected:
1. Determine the conformance level: Supports / Partially Supports / Does Not Support / Not Applicable
2. Write a clear, professional "Remarks and Explanations" text (1–3 sentences) that:
   - Describes what works (for Partially Supports)
   - Describes the specific failure and its scope
   - Is written for a procurement audience (not developers)
   - Avoids vague language like "some issues exist"
   - Does NOT include internal ticket numbers or code details

**Output format for each criterion:**
| SC ID | Criterion name | Conformance Level | Remarks |
|-------|---------------|-------------------|---------|

**After the table, also provide:**
- Recommended overall conformance statement: "Partially Conforms / Does Not Conform / Fully Conforms to WCAG [version] Level AA"
- Executive summary (3 sentences, plain language, suitable for legal/procurement review)

**Audit Findings:**
[PASTE YOUR AUDIT FINDINGS HERE — can be a list of issues, axe report, or audit table]

**Product context:**
- Product name: [NAME]
- Primary user base: [e.g., enterprise employees, general public]
- Technologies: [e.g., React SPA, server-rendered PHP]
```

---

## Tips

- The more specific your findings, the more accurate the VPAT entries.
- Include severity counts (Critical: 2, Serious: 5, Moderate: 3, Minor: 1) for better
  conformance statement accuracy.
- Use the `templates/vpat-2.5-template.md` to paste the generated entries directly.
- Review the output with your legal/compliance team before publishing.
