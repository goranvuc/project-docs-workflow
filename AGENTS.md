# Maintaining Project Docs Workflow

This repository distributes one Codex skill. Read README.md, the requested skill/reference/template, and its counterpart in README.sr.md when changing public guidance.

- Keep the supported scope focused on repository documentation workflows in Codex.
- SKILL.md owns agent-facing routing and constraints; mode-specific procedures live in its references. Templates are adaptable output assets, not a second authority.
- README.md and README.sr.md must describe the same capability, installation source, behavior, and limitations.
- Preserve source-user privacy: examples are fictional and contain no private project receipts, personal machine paths, credentials, or internal decisions.
- Do not add a topic document, dependency, helper script, approval gate, or required ceremony without a concrete need.
- Use one writer in a shared checkout. Behavioral evaluations run in isolated temporary fixtures outside the repository.
- Run `python scripts/validate.py` and the official skill-creator validator when available. Structural success is not behavioral validation; use realistic scenarios after material workflow changes.
- Record material validation outcomes in docs/validation.md. Do not claim remote publication, installation, or cross-platform behavior without its own evidence.
- Preserve user authorization boundaries for publication. Inspect the complete staged scope before committing and pushing.
