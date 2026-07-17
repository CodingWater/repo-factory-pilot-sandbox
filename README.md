# repo-factory-pilot-sandbox

Disposable sandbox for testing whether Repo Factory Protocol can guide fresh AI agents through bounded software work without prior chat context.

## Pilot product

The sandbox will become a tiny Python title-processing library across three genuine work cycles:

1. Generate URL-safe slugs.
2. Validate titles.
3. Render a Markdown title summary while testing resistance to unrelated cleanup.

The code is intentionally small. The real subject of the experiment is whether a fresh agent can understand authority, scope, evidence, stop conditions, and handoff state from the repository itself.

## Repo Factory Protocol

This repository uses Repo Factory Protocol v0.1, a repository-native operating environment for human-directed, AI-assisted software development.

A fresh implementation agent must read, in order:

1. `repo_control.md`
2. the matching human-authored work request
3. `AGENTS.md`

The agent then inspects only the source files and tests relevant to the active work.

## Core workflow

1. **Blueprint:** the human defines and activates bounded steps.
2. **Task:** the human opens a matching work request with frozen scope.
3. **Record:** the agent implements on a branch and appends its work entry before review.
4. **Stage:** the pull request stages the post-merge repository state.
5. **Human review and merge decision:** the human issues Merge, Repair, Reject, Split, or Quarantine and alone controls merge.
6. **Continue:** the merged repository state tells the next agent what is active.

## Authority split

| Role | Owns |
|---|---|
| Human | Product purpose, blueprint, scope, exceptions, verdict, and merge |
| Agent | Bounded implementation, checks, recording, evidence, self-review, and change proposal |

Agents do not invent scope and do not merge.

## Control files

| File | Purpose |
|---|---|
| `repo_control.md` | Project purpose, current state, active step, authority, and blueprint |
| `AGENTS.md` | Agent behavior and scope constraints |
| `agent_record.md` | Append-only work history and current project summary |
| `docs/product_spec.md` | Repo Factory Protocol v0.1 product contract and limits |
| `.github/ISSUE_TEMPLATE/work_request.md` | Human work contract template |
| `.github/pull_request_template.md` | Criterion-to-evidence review packet |

## Merge verdicts

- **Merge:** correct, complete, and safe to merge.
- **Repair:** specific defects must be fixed first.
- **Reject:** wrong, unnecessary, or harmful.
- **Split:** too broad and must be divided.
- **Quarantine:** required context or evidence is unavailable.

## Pilot rule

Do not explain the original planning history to the blind agent. Give it the repository and active work request, then observe whether the repository carries the workflow.
