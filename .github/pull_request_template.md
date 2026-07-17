## Exact blueprint step

[Copy the exact step number and title from `repo_control.md`.]

## Purpose

[Why is this change needed? What does it accomplish?]

## Scope

- [ ] This pull request implements exactly one blueprint step.
- [ ] Every changed file is allowed by the linked work request.
- [ ] No dependencies, automation, or tooling were added unless required by the step.

## Files changed

| File | Action | Reason |
|---|---|---|
| `path/to/file` | created / updated | [why] |

## Acceptance criteria and evidence

<!-- Include every frozen criterion from the linked work request. Mark unmet criteria honestly. -->

| Criterion | Status: met / unmet | Evidence |
|---|---|---|
| [criterion] | [status] | [file, diff, command, or review evidence] |

## Automated checks

<!-- For every automated check used, state its result, what it proves, and what it does not prove. Write "None" if no automated checks were used. -->

| Check | Result | What it proves | What it does not prove |
|---|---|---|---|
| `[command or check]` | pass / fail / not run | [bounded claim] | [explicit limitation] |

## Material uncertainty

- **Assumptions:** [material assumptions or "None known"]
- **Unknowns:** [material unknowns or "None known"]
- **External dependencies:** [relevant external dependencies or "None"]
- **Conflicts or risks discovered:** [material conflicts/risks or "None known"]

## Exact commit reviewed

`[full commit SHA]`

- [ ] The complete diff at this exact commit was self-reviewed after all repairs.

## Agent record and staged state

- [ ] `agent_record.md` contains a sequential entry for this work.
- [ ] The current step is staged as `done`.
- [ ] The next already-defined planned step is staged as `active`, or no active step remains when none exists.
- [ ] The project summary matches the staged post-merge state.
- [ ] These staged changes remain provisional until human merge.

## Self-review

- [ ] Every changed file belongs to the active work request.
- [ ] No scope expansion occurred.
- [ ] Files are internally consistent in terminology, authority, and current state.
- [ ] Unmet criteria and material uncertainty are visible rather than hidden.
- [ ] A fresh agent can identify what happens next.
- [ ] Human-only merge authority remains intact.

## Merge verdict

[Pick exactly one: Merge | Repair | Reject | Split | Quarantine]

## Steps remaining

[List remaining blueprint steps or "None" if this was the final step.]
