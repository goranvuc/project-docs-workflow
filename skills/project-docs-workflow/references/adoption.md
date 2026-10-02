# Establish or adapt a documentation workflow

Use this reference only when the user requests setup, adaptation, or documentation reorganization. Assessment remains read-only unless the user also authorizes changes.

## Inventory before writing

Follow local repository instructions. Identify existing document roles, active work, accepted decisions, and verification commands. Inspect enough implementation to ground the overview; do not turn setup into an unrelated repository-wide audit.

Record a compact mapping in your working notes: role → current file/section → destination or reason to retain its location. Reuse useful content, names, and roles; do not treat an existing path alone as a reason to keep it. An existing roadmap with statuses and completion criteria can serve as the active plan, moved into the documentation home when appropriate; do not add a competing `plan.md`.

## Choose the documentation home

During setup, adaptation, or requested reorganization, bring maintained project documentation together under `docs/` by default. This includes existing standalone setup, architecture, operational, and model-validation guides, even when they currently sit at the root. For example, root `INTEGRATION-SETUP.md` and `MODEL-CHECKS.md` normally become `docs/INTEGRATION-SETUP.md` and `docs/MODEL-CHECKS.md`, with their useful content preserved.

Keep root entry documents such as `README.md`, `AGENTS.md`, and `CLAUDE.md` in place. Preserve required or conventional locations for files such as `LICENSE`, repository policy files, tool configuration, and package-local agent instructions. Do not relocate every Markdown file indiscriminately.

Use a different documentation location when there is a concrete reason: an explicit local contract, an established equivalent directory such as `handbook/`, a tool that requires a path, or documentation maintained beside its package in a monorepo. Record the chosen home and any exceptions with their reasons in the local map/instructions. Resolve a conflict with an accepted path rule before dependent moves; routine organization already authorized by the request needs no extra approval.

A tiny project may keep its short overview, plan, and session sections together in the root README. Do not create empty documents just to populate `docs/`. Existing substantive standalone guides, however, should move to the chosen documentation home unless a concrete exception applies. Read-only assessment only recommends moves, and journal consolidation alone does not authorize an unrelated reorganization.

For a project with no structure, a practical starting point is:

```text
AGENTS.md
README.md                 # can also contain the short project overview
docs/plan.md
docs/journal/README.md
docs/journal/<session>.md
```

Create `docs/journal/archive/` when a record is actually processed. Add focused documents when a subject needs a stable contract. No minimum number of files or mandatory technology-specific topics applies.

## Adopt deliberately

Adapt the linked templates to the observed project. Use the existing document language. Template braces are authoring placeholders and must be replaced before delivery.

Ensure the local instructions state:

- Which files own which roles and in what order to read them.
- The maintained documentation home and reasons for any location exceptions.
- Which session types leave a journal and where its single canonical template lives.
- When related plan updates happen and when stable contracts are consolidated.
- How open findings survive archival.
- Actual verification commands and their limits, or the current manual procedure if no checker exists.
- Existing publication and external-action boundaries without importing permissions from this skill.

If existing rules conflict with the requested adoption, show the concrete difference. Preserve accepted decisions; resolve only the missing owner choice. Do not demand approval for routine file naming or work already within the request.

## Migrate existing information

Preserve evidence and document the destination of moved content. Separate present implementation from accepted intent and proposals. Give scheduled work one operational home, while preserving reference links from risk inventories and records.

Do not create fictional historical sessions, fabricated timestamps, unknown test results, or invented commit hashes. If provenance is unavailable, say so. Do not archive uncertain material to make the directory look tidy. Preserve older formats unless the task requires their migration.

Before moving files, map old paths to new paths and check for destination collisions; never overwrite unrelated content or leave duplicate authoritative copies. Repair incoming links, outgoing relative links and assets, navigation, and path references in relevant scripts, configuration, or CI. Search for old paths and account for remaining occurrences, preserving historical evidence where appropriate. If tooling depends on a path, repair that reference within the authorized scope or retain the path with a recorded reason. Verify that live references resolve and the original content survives the move.

Use anchored sections or durable task IDs for open findings. A file-level link is sufficient only when the target clearly identifies the transferred content.

## Finish

Read the result as a new contributor would: can they find project purpose, accepted constraints, the next authorized work, and the limits of existing evidence? Inspect for duplicated rules and parallel backlogs. Verify local links and supplied commands without running unrelated mutation or paid operations.

Leave one session record when required by the adopted contract, including remaining decisions and pending documentation. Report the resulting map and how to invoke a future documentation phase. Do not describe installation, publication, or deployment as done unless separately performed and checked.
