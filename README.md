# Project Docs Workflow

**Keep project decisions, plans, and evidence useful across Codex sessions.**

[Srpski](README.sr.md) · [Install](#install-in-codex) · [Try it](#first-use) · [Working discipline](#the-discipline-that-makes-it-work) · [Validation](docs/validation.md)

A Codex skill for establishing and maintaining a small, coherent documentation workflow. It gives project rules, accepted decisions, planned work, and session evidence clear homes, then helps move new knowledge into maintained documentation without losing unfinished work.

It is useful when a project spans many sessions, contributors, or agents and reconstructing **what exists, what was decided, and what comes next** starts taking effort.

**The benefit:** a clear starting point, one operational plan, and a traceable handoff between sessions. **The commitment:** decisions must be made explicit, meaningful work recorded, and accumulated notes consolidated. Installing a skill does not keep documentation current by itself.

## What changes in practice

| Recurring problem | How this workflow addresses it |
|---|---|
| A new session starts by guessing which document is current | A short overview points to the authoritative source for each role |
| Tasks live in a roadmap, several reviews, and unfinished chat threads | One active plan owns work order, dependencies, and completion criteria |
| A suggestion gradually becomes an assumed product decision | Proposals, accepted decisions, and actual behavior stay distinguishable |
| A successful local test becomes “ready for production” | Each claim records the evidence it actually has |
| Old session notes are either reread forever or discarded | Verified knowledge is transferred, open work gets a destination, and the original evidence is archived |

For example, a session discovers that CSV export drops leading zeros. The approved contract still requires preserving identifiers. A documentation phase records the deviation, transfers the repair to an open plan item, and links the original evidence. The journal can then be archived while the repair remains explicitly open.

The workflow supports long-lived repositories. A small prototype may need only a short overview, a plan, and session records. There is no mandatory stack, fixed catalog of documents, or new project-management service.

During setup or adaptation, maintained project documentation is brought together under `docs/` by default, including standalone guides previously scattered at the root. **Preserving useful content does not require preserving its path.** A move includes repairing links and relevant script/configuration references. Root entry documents such as `README.md`, `AGENTS.md`, and `CLAUDE.md` stay in place. Concrete exceptions, including tool-required paths or an established equivalent documentation directory, are recorded in the local map. A tiny project may still combine roles in its README. Assessment only recommends changes; routine journal consolidation does not trigger a reorganization.

## Install in Codex

**You do not need a local copy of this repository.** Open a Codex conversation with network access and paste this message:

```text
Use $skill-installer to install the project-docs-workflow skill from:
https://github.com/goranvuc/project-docs-workflow/tree/main/skills/project-docs-workflow

Install it for my user so it is available across my local Codex projects,
and report the actual installation directory.
```

This is a message to Codex, not a terminal command. Its bundled Skill Installer downloads the skill folder, including its references and templates. No manual clone or package build is needed. See the [official Codex skill instructions](https://learn.chatgpt.com/docs/build-skills).

The bundled installer inspected for this release defaults to:

```text
$CODEX_HOME/skills/project-docs-workflow/
```

When `CODEX_HOME` is unset, that is `~/.codex/skills/project-docs-workflow/`; on Windows, normally `%USERPROFILE%\.codex\skills\project-docs-workflow\`. Use the actual path reported by your installer. Codex also supports `.agents/skills` locations; you do not need to move a successfully installed skill between directories.

In your next message, verify discovery without changing a project:

```text
Use $project-docs-workflow. Describe its supported operations and confirm
the path of the SKILL.md you loaded. Do not change any files.
```

If Codex cannot discover it, restart Codex and try again. If `$skill-installer` itself is unavailable, use the manual fallback below. Installation makes the skill available; applying it to a repository is a separate request.

<details>
<summary>Manual installation and troubleshooting</summary>

Download the repository ZIP from GitHub, extract it, and copy the **whole** `skills/project-docs-workflow` directory into your user skills directory, such as `~/.agents/skills/`. The resulting path must be `~/.agents/skills/project-docs-workflow/SKILL.md`.

For a repository-local installation, use `<repository>/.agents/skills/project-docs-workflow/`. Keep one active installed copy per intended scope; duplicate names can make selection confusing. Do not copy only `SKILL.md`, and do not copy the entire repository into a nested skill folder.

For repeatable installation, use a published tag or commit SHA in the GitHub URL instead of `main`. A local installation does not automatically install the skill on another computer or remote host.

</details>

### Updating an installed copy

The inspected installer refuses to overwrite an existing destination. It is not an automatic updater, and changes on GitHub do not update your installed copy.

Ask Codex to compare your installed copy with the desired GitHub revision, preserve any local customizations, and install the new version into a temporary directory. After review, replace the old copy while keeping a recoverable backup **outside scanned skills directories**. Verify discovery again. Do not delete a customized installation just to get past an “already exists” error.

## First use

Start with an assessment when joining an existing project:

```text
Use $project-docs-workflow to assess this repository's documentation.
Identify conflicting authorities, duplicated plans, and missing handoff evidence.
Recommend the smallest useful changes. Do not modify files.
```

To establish the workflow in a new project:

```text
Use $project-docs-workflow to establish a minimal documentation workflow here.
Adapt it to the actual project and keep the local agent instructions self-contained.
```

To adapt an established repository:

```text
Use $project-docs-workflow to adapt the existing documentation workflow.
Preserve accepted decisions and useful content. Map existing files to roles
before adding new ones, and keep a single operational plan.
```

To process accumulated session evidence:

```text
Use $project-docs-workflow for a documentation phase over the active journals.
Reconcile current evidence and accepted decisions, update relevant contracts
and the plan, and archive only records whose material content has a verified
destination. Keep unfinished implementation work open.
```

Ordinary feature work then follows the repository's local instructions. You do not need to invoke this skill in every coding prompt. A one-paragraph prose edit does not require a full documentation phase.

## How the pieces fit together

| Role | Owns |
|---|---|
| Local `AGENTS.md` | Reading order, work boundaries, and the adopted lifecycle |
| Short overview / map | Project context and navigation |
| Active plan | Priorities, dependencies, owner decisions, and completion evidence |
| Focused contracts | Current behavior, accepted intent, and known deviations |
| Active journal | Meaningful session outcomes and pending knowledge transfer |
| Processed archive | Preserved evidence with explicit destinations |

These are roles, not a required file count. The skill helps establish or apply the process; local project instructions remain the durable authority for ordinary work. Accepted project rules take precedence over generic templates.

```text
Meaningful work → session record → documentation phase → processed archive
                       │                   │
                       └── related plan updates
                                           └── contracts + explicit open tasks
```

An archive records that knowledge was accounted for. An implementation task closes only when its own completion criteria are supported.

## The discipline that makes it work

This approach requires a maintainer who makes decisions and reviews evidence. The agent can organize information and apply the workflow; responsibility for the project remains with its owner and contributors.

1. **Keep one operational plan.** Prioritize and close work there. Journals and risk inventories may link to tasks; they should not become competing backlogs.
2. **Make decisions explicit.** Label proposals and accepted choices. When a choice changes, record what supersedes it and what the change affects.
3. **Record meaningful sessions.** Capture outcomes, checks, pending documentation, and open work. Avoid transcripts of every command and a new record for every trivial edit or question.
4. **Consolidate before notes become a burden.** Request a documentation phase at useful milestones or when the active records make the next session hard to start. Keep the cadence proportionate to the project.
5. **Preserve unresolved findings.** Before archiving, give each material item an inspectable destination. Open work must remain visible after its source journal moves.
6. **Use precise evidence labels.** Implemented, locally tested, committed, pushed, deployed, and live-verified are different claims. State failures, skipped checks, and uncertainty.
7. **Review meaning as well as links.** A structurally valid document can still contain an incorrect claim or an omitted finding. Check the source-to-destination transfer.
8. **Respect scope and ownership.** Documentation work does not authorize implementing every finding, publishing a repository, deploying a service, or altering live data. Existing authorization remains valid; do not add repeated approval steps to routine work.

If decisions stay only in chat and consolidation never happens, the process will drift. More templates will not correct that. Keep the documents small enough to read and the commitments realistic enough to maintain.

## Scope and limitations

- The skill assesses, establishes/adapts, consolidates, and validates documentation workflows in Codex. Other agent platforms are not a tested support target for this release.
- It does not run in the background, schedule maintenance, synchronize installed copies, or apply itself to every repository.
- It does not supply a universal project documentation checker. It uses existing checks where available and calls for manual structural and semantic review otherwise.
- It does not certify release readiness, correctness, security, or legal compliance. Read the recorded [validation scope](docs/validation.md).
- It preserves a project's existing authorization rules. Installing the skill grants no repository, account, deployment, or data permissions.

## Package and contributing

The installable package is [`skills/project-docs-workflow/`](skills/project-docs-workflow/SKILL.md). It contains the core instructions, two focused references, four adaptable templates, and Codex UI metadata. The public README files and repository validation tools are maintained alongside it and are not copied by the normal skill-folder installation.

For a local source checkout, Python 3.10+ can run the repository's dependency-free structural check:

```text
python scripts/validate.py
```

This checks package structure, required metadata, and relative Markdown links/anchors outside fenced examples. It does not check external URLs or whether an agent makes good decisions. Material workflow changes also need realistic behavioral exercises in isolated fixtures. See [maintainer guidance](AGENTS.md) and [validation evidence](docs/validation.md).

When proposing a change, include the concrete workflow problem, a small example, and its effect on existing projects. Keep the English and Serbian README versions aligned. Prefer demonstrated needs over more rules for hypothetical edge cases.

## License

[MIT](LICENSE). You may use, adapt, and redistribute the package under its terms. This project is independently maintained and is not an official OpenAI product.
