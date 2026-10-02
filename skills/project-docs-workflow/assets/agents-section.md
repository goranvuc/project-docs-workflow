<!-- Template: adapt this section into existing project instructions. Replace every {{...}} placeholder, preserve accepted rules, and remove this comment. Do not copy it over an existing AGENTS.md. -->

## Documentation authority and reading order

These local instructions own the documentation lifecycle. The journal README at `{{journal_readme}}` owns the single session template. The short overview at `{{overview}}` maps the maintained documents. `{{active_plan}}` is the sole operational source for priorities, dependencies, open decisions, and completion criteria.

Maintain project documentation under `{{documentation_directory}}`. Keep root entry documents such as `README.md`, `AGENTS.md`, and `CLAUDE.md` in place; record any other location exceptions and their concrete reasons in the overview. Put new focused documents in the documentation home. Relocation belongs to an authorized setup/adaptation or reorganization; preserve useful content and repair affected links and tool/configuration references when moving files.

Start with the overview. Read the plan when selecting, advancing, closing, adding, or reprioritizing work. Read full active entries under `{{journal_directory}}`, excluding the template, then the relevant focused contracts. Keep the active set small through documentation phases. Read archives only for a requested historical lookup or a directly relevant linked receipt.

Code describes actual behavior; accepted decisions describe intended behavior. Preserve a decision when the implementation deviates and record the defect. Distinguish proposals, accepted decisions, implementation, local checks, commits, publication, deployment, and dated live evidence.

## Normal work

Change files relevant to the authorized task. Update the active plan when its related status, scope, order, dependencies, or completion criteria actually change. For a meaningful implementation or planning/decision session, create one journal with outcomes, verification, pending stable-document updates, and remaining work. Follow explicit documentation requests within their scope; otherwise transfer stable-document changes in a documentation phase.

Ad hoc read-only assessments end with an answer and no repository changes. Create a durable review record only when requested. One journal belongs to the session, not to each finding or subagent. Use one writer in a shared checkout or isolated worktrees for parallel writers; read-only reviewers must not run cache-writing checks or servers in the shared checkout.

## Documentation phase

Read complete in-scope active journals, the plan, relevant contracts, and supporting implementation. Reconcile newer accepted decisions. Every material finding needs an exact destination: updated contract, open task, linked duplicate, evidenced resolution, or reasoned rejection.

Preserve original evidence and append absorption destinations before archiving. An archived journal can contain an open problem when that problem is fully transferred to the active plan. A finding without a reliable destination keeps the journal active. Physically move processed records to `{{archive_directory}}` and verify the move and affected links.

Create one record for the documentation session. It may be archived in the same phase if all its content is already absorbed with explicit references. Avoid duplicate records for the same session.

## Checks and permission boundaries

{{actual_documentation_checks_or_manual_procedure}}

Structural checks do not prove claim accuracy, complete transfer, implementation correctness, or release readiness. Review meaning separately. Preserve the project's existing authorization boundaries for commit/push, deployment, cloud changes, paid calls, messages, and destructive operations. This documentation workflow adds no permission and requires no repeated approval for already authorized work.
