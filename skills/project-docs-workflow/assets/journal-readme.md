<!-- Template: adapt to existing metadata rather than migrating old records automatically. Replace {{...}} and remove this comment. -->

# Session journal

Local agent instructions define when a record is required. This file is the single source for its format. Create one record per meaningful implementation, planning/decision, or documentation session. Read-only assessments produce no record unless a durable report is requested.

## New record

Location: `{{journal_directory}}/YYYY-MM-DD_HHMM-short-slug.md`.

```yaml
---
title: "Concrete session outcome"
date: "YYYY-MM-DD"
status: "completed"
work_type: "implementation"
docs_updated: false
docs_update_required: true
archived: false
---
```

Use the actual date and session status. `status` describes the session, not feature or release completion. `work_type` is a short description, not a fixed enum. Add useful provenance such as timestamps with timezone, branch, commit, agent, and operator only when known; do not fabricate it. Set `docs_update_required: false` with a reason when there is no pending durable transfer.

Use these sections:

1. **Purpose and scope** — requested outcome and boundaries.
2. **Changes** — actual results and relevant paths.
3. **Decisions** — accepted decisions, proposals, and unresolved choices distinguished.
4. **Verification** — exact checks and results; identify local, mock, live, or unavailable evidence.
5. **Pending documentation** — content and intended destinations, or a reason no transfer is needed.
6. **Open work and handoff** — plan IDs, remaining work, dependencies, and next boundary.

## Absorption and archive

Preserve the original record. After every material item has a verified destination, set:

```yaml
docs_updated: true
docs_update_required: false
archived: true
```

Append a `Documentation absorption` section with the actual processing date and a table:

| Source item | Destination | Disposition and remaining work |
|---|---|---|
| Specific decision or finding | Exact file/section or task ID, linked from the final archive location | Updated, open, duplicate, resolved with evidence, or rejected with reason |

For a no-change record, explain why no durable transfer is needed and link to the session/decision that accounts for it. `docs_updated: true` records completed absorption, including this disposition; it does not claim every document changed.

Move to `{{archive_directory}}` only after transfer verification. Check moved content, incoming links, and relative links from the archive. A remaining implementation task stays open in the plan; an item without a reliable destination keeps the journal active. Older formats remain historical unless migration was requested.
