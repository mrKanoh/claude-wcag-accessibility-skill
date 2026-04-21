# Security Policy

## Supported Versions

This is a Claude Code skill — a collection of documentation, data files, and scripts.
There is no running server or network-facing application. The attack surface is limited to:

- `scripts/search.py` — reads local CSV files; no network access, no exec/eval
- `scripts/generate-resources-md.py` — reads/writes local files only
- `tests/test_search.py` — executes search.py as a subprocess
- HTML component examples — static files, no backend

| Component | Supported |
|-----------|-----------|
| `scripts/search.py` | ✅ Latest `main` branch |
| HTML component examples | ✅ Latest `main` branch |
| `.github/workflows/` | ✅ Latest `main` branch |

## Reporting a Vulnerability

If you discover a security issue (e.g., a script that could be exploited for path traversal,
code injection in a CI workflow, or a malicious dependency), please **do not** open a public
GitHub issue.

Instead, report it privately via one of these channels:

1. **GitHub private vulnerability reporting** (preferred):  
   Go to the [Security tab](https://github.com/mrKanoh/claude-wcag-accessibility-skill/security/advisories/new)
   and click "Report a vulnerability"

2. **Email**: Open a GitHub Discussion and request a private contact if GitHub security
   reporting is unavailable for your account

### What to include

- Description of the vulnerability and its potential impact
- Steps to reproduce
- Affected file(s) and line number(s)
- Suggested fix if you have one

### Response timeline

- We aim to acknowledge reports within **48 hours**
- We aim to publish a fix within **7 days** for critical issues
- We'll credit reporters in the release notes unless you prefer to remain anonymous

## Scope

The following are **out of scope** for security reports:

- Issues in axe-core, Playwright, pa11y, or other third-party tools referenced in templates
  (report those upstream)
- Missing HTTP security headers (this project has no web server)
- Theoretical attacks that require physical access to the machine running the scripts

Thank you for helping keep this project safe. ♿
