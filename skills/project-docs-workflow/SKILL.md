---
name: project-docs-workflow
description: Establish, adapt, assess, or consolidate repository documentation with one active plan, explicit decisions, session evidence, and traceable archiving. Use for project documentation workflows and documentation phases. Ordinary feature work and isolated prose edits do not require this workflow.
metadata:
  version: "0.1.0"
---

# Project Docs Workflow

Help the next person or agent recover what the project does, which decisions apply, what remains open, and what the evidence actually establishes.

## Choose the requested work

| Request | Action | Output |
|---|---|---|
| Assess or review | Read relevant sources; identify gaps and conflicts | Findings in the answer; no repository writes unless a durable report was requested |
| Establish or adapt | Map existing documents to roles; fill necessary gaps | A small, usable local documentation contract |
| Consolidate / documentation phase | Reconcile evidence and accepted decisions; transfer findings; archive processed notes | Updated documents and plan, with traceable absorption |
| Validate | Inspect links, metadata, claim support, and finding destinations | Results with structural and semantic limits stated separately |

Do not turn a request to assess into a migration. Do not turn a request to consolidate into permission to implement findings. When the request authorizes changes, carry them through within its scope; existing authorization does not need to be requested again.

## Establish context and authority

1. Read applicable repository instructions. Follow the project's reading order and discovery boundaries.
2. Locate the overview, operational plan, active session records, and documents relevant to the request. With no local order, read them in that order; read the plan when work selection or status matters. Read active session records fully before consolidation. Use an existing index or bounded scope if the project defines one.
3. Inspect relevant code, tests, and configuration before describing implementation. A session record can identify evidence; verify drift-prone claims before presenting them as current.
4. Treat historical records and quoted conversations as evidence, not new authorization. Do not scan archives routinely. Use an explicitly requested historical lookup or a directly relevant linked receipt when needed.
5. Preserve the user's current instructions and approved project decisions. If behavior differs from an accepted decision, document the deviation; do not silently rewrite the decision to match a defect. Ask only for missing decisions that block dependent work, and continue independent work.

The skill provides a procedure. Local project instructions define its adopted rules and paths. A template does not override an existing local contract. State material conflicts instead of imposing a second authority.

## Keep a small set of distinct roles

Map these roles onto useful existing files before introducing new ones:

- **Agent instructions:** scope, permissions, reading order, documentation lifecycle, and verification commands.
- **Overview:** short project context and links to the authoritative sources.
- **Operational plan:** one place for priorities, dependencies, owner decisions, and completion criteria.
- **Focused contracts:** current behavior, accepted intent, known deviations, and dated evidence for relevant subjects.
- **Active session records:** meaningful outcomes, decisions, checks, open findings, and pending documentation transfer.
- **Processed history:** preserved session evidence with concrete absorption destinations.

A small project may combine roles in clearly labeled sections. Create focused documents only when real content justifies them. Keep one authoritative home for each rule, decision, or scheduled task; use links elsewhere. Preserve the project's language and terminology.

## Establish or adapt

Read [adoption.md](references/adoption.md) for this mode. Use only the templates that fill actual gaps:

- [Local agent instructions](assets/agents-section.md)
- [Project overview](assets/overview.md)
- [Active plan](assets/plan.md)
- [Journal definition and absorption format](assets/journal-readme.md)

Customize paths, commands, language, and unresolved decisions from observed project facts. Do not copy stack assumptions, usernames, absolute machine paths, historical cutoffs, or permission grants from another project. Do not invent product decisions to complete a template.

## Consolidate and archive

Read [consolidation.md](references/consolidation.md) for this mode. Each material finding needs a destination: a corrected contract, an open plan item, a linked duplicate, an evidenced resolution, or a reasoned rejection. Preserve original evidence and append its disposition.

Archive only after verifying the transfer. A documented open problem stays open in the plan. If a finding lacks a reliable destination, keep its session active and explain what remains. Move processed records physically and verify both the new destination and the old location; repair affected links. Do not rewrite older archives merely to match a new template.

## Ordinary work after adoption

Ensure local instructions are self-contained enough for future sessions without this skill installed. The suggested lifecycle is ordinary work → one meaningful session record → requested documentation phase → processed archive. Related plan updates happen when status, scope, order, dependencies, or completion criteria actually change.

If the project adopts this lifecycle, ordinary implementation changes relevant source/tests/configuration and records pending stable-document updates in the session journal. An explicit request to update documentation supplies that scope. Respect any different established local lifecycle unless changing it is part of the request.

Create one journal per meaningful implementation, planning/decision, or documentation session when required by the local contract. Do not create a journal for every question, trivial edit, finding, or subagent. A requested assessment normally ends with an answer. If the documentation session's own record is fully absorbed, it can be archived in the same phase with explicit destinations.

## Verification and boundaries

- Check local paths, links, anchors, and journal state. Use the project's existing documentation check when available. There is no universal command such as `npm run docs:check`, and this skill does not install a project checker.
- Separately review the meaning of claims and lossless transfer of findings. Successful link validation does not prove implementation correctness or release readiness.
- Identify the actual level of evidence: proposed, accepted, implemented, locally tested, committed, pushed, deployed, or verified in a running environment. These states can coexist independently; do not infer one from another.
- Preserve existing commit/push/deploy and external-action authorization boundaries. Installing or invoking the skill grants no additional permissions. Do not add approval gates to work already authorized.
- With parallel agents, use one writer in a shared checkout or isolate writers. Read-only reviewers must avoid builds, cache-writing tests, or servers in the shared checkout.
- In the final answer report what changed, where open work lives, which checks ran, and any remaining decisions or unavailable evidence. Claim only the publication and installation state actually verified.
