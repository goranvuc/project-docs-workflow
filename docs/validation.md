# Validation scope and evidence

Date: 2026-10-02. Package version: 0.1.0. These are observed checks of this distribution, not guarantees about projects that later adopt it.

## Local structural checks

- The bundled Codex skill-creator `quick_validate.py` accepted the installable skill. Its PyYAML dependency was supplied in a temporary validation directory; the distributed skill has no Python dependency.
- `python scripts/validate.py` passed for package structure, required metadata, and local Markdown links/anchors. This repository tool requires Python 3.10+ with the standard library only.
- Isolated negative probes confirmed that the validator rejects a missing link destination, a nonexistent anchor, and a skill name that differs from its directory. The unchanged package passed the same runner.
- Staged whitespace checks passed. The distribution was reviewed for unrelated project content and private machine-specific data.

## Behavioral exercises

Two evaluating agents were given the skill, raw synthetic fixtures, and realistic requests without the author's expected answers. Writes were restricted to separate temporary fixture directories. The author inspected the resulting documents and source preservation.

| Scenario | Observed result |
|---|---|
| Establish a minimal workflow for a tiny line-counting utility | The evaluator used two maintained documents, combining roles in README sections instead of imposing a documentation tree. Source inspection exposed a claimed CLI capability absent from the supplied function; intended scope stayed explicit and the decision remained open. Source was unchanged. |
| Assess inconsistent documentation without write authorization | The evaluator reported the unsupported task-completion claim and unaccepted priority proposal without modifying files. Before/after SHA-256 values matched for all four fixture files. |
| Consolidate an existing project with custom document paths | The evaluator retained the existing plan and contract, transferred the leading-zero export defect to an open task, preserved an XLSX idea as an unaccepted owner decision, and physically archived the source plus one documentation-session record with destinations. Application source remained unchanged. |

In the consolidation exercise, a final structural check detected a generated absorption-anchor mismatch. The evaluator repaired it before completing the exercise; the final check passed for 29 relative links/anchors across seven Markdown files. This is evidence for keeping verification in the workflow, not evidence that generated links are always correct.

These were single-pass, bounded synthetic exercises. They do not establish reliability across every repository, model, language, historical format, or conflict. No application runtime tests, live systems, or deployments were part of the exercises.

## Editorial review

A separate read-only review compared the English and Serbian README versions against the actual skill package. One Serbian prompt incorrectly meant "least useful changes"; it was corrected to request the smallest useful set of changes. No other material parity or capability mismatch was identified in that review.

## Package identity

The tested installable package contains eight files. Its SHA-256 bundle fingerprint is:

```text
b4d314b771f968912796ee7371b857080a3dc19e4e5c77e3c91dacf1c2b72718
```

Fingerprint method: sort relative file path strings lexicographically, case-sensitively; feed each UTF-8 path with `/` separators, a NUL byte, the file bytes, and another NUL byte into SHA-256. The fingerprint covers `skills/project-docs-workflow/` only, so editorial updates outside that directory do not change the tested skill identity.

## GitHub and installation evidence

- The repository was created as public at [goranvuc/project-docs-workflow](https://github.com/goranvuc/project-docs-workflow), with `main` as its default branch. The first published revision was `05975eabb92057215b5635e538504c262bb79f6d`; the local and remote branch values matched.
- GitHub Actions completed its structural validation successfully for that revision: [recorded run](https://github.com/goranvuc/project-docs-workflow/actions/runs/37021703928).
- The bundled Codex Skill Installer was run with the README's GitHub folder URL, `--method download`, and an empty temporary destination. It downloaded the remote package successfully; no local source checkout was used by the installer. SHA-256 comparison confirmed that all eight downloaded files matched the reviewed source byte-for-byte.
- The same remote download was then installed into the default user directory, `$CODEX_HOME/skills/project-docs-workflow/`. All eight installed files matched the reviewed source byte-for-byte. No existing installation was overwritten.
- These are download and on-disk installation checks. Discovery through a subsequent interactive Codex turn was not separately exercised during this publication session; the README includes the exact non-mutating prompt for that check.

## Limits and maintenance

Structural validation does not check external URLs, template customization, claim truth, semantic transfer, or agent judgment. Review these separately. The built-in installer was inspected for its GitHub-folder interface, destination handling, and refusal to overwrite an existing installation. Other installer versions may differ; use the actual path and result reported by Codex.

Repeat affected checks after meaningful changes. For workflow changes, use realistic requests in isolated fixtures and inspect the outcomes. Keep repository validation, behavioral validation, publication, installation, and discovery evidence distinct.
