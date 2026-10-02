# Establish or adapt a documentation workflow

Use this reference only when the user requests setup or adaptation. Assessment remains read-only unless the user also authorizes changes.

## Inventory before writing

Follow local repository instructions. Identify existing document roles, active work, accepted decisions, and verification commands. Inspect enough implementation to ground the overview; do not turn setup into an unrelated repository-wide audit.

Record a compact mapping in your working notes: role → current file/section → needed change. Reuse names and locations that already work. For example, an existing roadmap with statuses and completion criteria can serve as the active plan; a new `plan.md` would create competing authority.

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
- Which session types leave a journal and where its single canonical template lives.
- When related plan updates happen and when stable contracts are consolidated.
- How open findings survive archival.
- Actual verification commands and their limits, or the current manual procedure if no checker exists.
- Existing publication and external-action boundaries without importing permissions from this skill.

If existing rules conflict with the requested adoption, show the concrete difference. Preserve accepted decisions; resolve only the missing owner choice. Do not demand approval for routine file naming or work already within the request.

## Migrate existing information

Preserve evidence and document the destination of moved content. Separate present implementation from accepted intent and proposals. Give scheduled work one operational home, while preserving reference links from risk inventories and records.

Do not create fictional historical sessions, fabricated timestamps, unknown test results, or invented commit hashes. If provenance is unavailable, say so. Do not archive uncertain material to make the directory look tidy. Preserve older formats unless the task requires their migration.

When moving files, check incoming and outgoing links. Use anchored sections or durable task IDs for open findings. A file-level link is sufficient only when the target clearly identifies the transferred content.

## Finish

Read the result as a new contributor would: can they find project purpose, accepted constraints, the next authorized work, and the limits of existing evidence? Inspect for duplicated rules and parallel backlogs. Verify local links and supplied commands without running unrelated mutation or paid operations.

Leave one session record when required by the adopted contract, including remaining decisions and pending documentation. Report the resulting map and how to invoke a future documentation phase. Do not describe installation, publication, or deployment as done unless separately performed and checked.
