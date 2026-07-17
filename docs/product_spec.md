# Repo Factory Protocol Product Specification v0.1

## Status

**Version:** v0.1

**State:** Product contract adopted for the external pilot.

This operating kernel is frozen through the three-cycle external adoption pilot. New conceptual questions belong in the protocol backlog unless they expose a false product claim, direct contradiction, security or authority defect, inability to identify the permitted action, or inability to perform authorised work safely.

## Product definition

Repo Factory Protocol is a repository-native operating environment for human-directed, AI-assisted software development.

It gives a capable fresh agent enough stable context to determine:

1. What project it has entered.
2. What work is currently authorised.
3. Which human request defines that work.
4. What the agent may and may not change.
5. What evidence must be produced.
6. What assumptions, unknowns, conflicts, or external dependencies affect the work.
7. Who holds final authority.
8. What must be recorded for the next agent.

The product reduces avoidable guesswork. It does not eliminate uncertainty, trust, owner authority, interpretive error, or human judgment.

## Product promise

At an authoritative repository commit, a capable fresh agent should be able to identify the permitted next action without access to previous conversation history.

When implementation is authorised, the agent should be able to identify its exact scope and required evidence.

When implementation is not authorised, the agent should be able to identify that it must not begin.

## Explicit limits

Repo Factory Protocol does not claim that:

1. Repository information is complete or objectively true.
2. A written constraint is automatically enforced.
3. Machine-readable declarations prove compliance.
4. Passing tests prove that the requested behaviour is correct.
5. A local checker is mandatory before merge.
6. Repository history is independently tamper-proof.
7. The protocol can prevent the repository owner from changing or deleting it.
8. Human judgment can be removed from governance.
9. Agents will never misunderstand clear instructions.
10. External systems are accurately represented unless they have been verified.
11. Every relevant fact can or should be stored inside the repository.
12. More governance automatically produces better work.

These are permanent system boundaries, not unfinished promises.

## Operating kernel

Every implementation agent must read, in order:

1. The current operating state in `repo_control.md`.
2. The matching human-authored work request.
3. `AGENTS.md`.

The agent then inspects the source files and tests relevant to the active work.

The agent reads historical records or external context only when the active work requires them. The full product specification is not part of ordinary agent startup.

Implementation must not begin unless an active human-approved step and matching human-authorised work request exist.

## Canonical authority

### `repo_control.md`

Owns project purpose, blueprint steps, step status, the active step, human authority, Human Blueprint Activation, and the permitted next action.

### Human-authored work request

Owns current task purpose, exact allowed files, forbidden changes, frozen acceptance criteria, required evidence, known assumptions, known material unknowns, relevant external dependencies, and stop conditions.

### `AGENTS.md`

Owns agent behaviour, mandatory startup sequence, scope discipline, recording requirements, review requirements, mechanical orchestration limits, and human-only merge authority.

### `agent_record.md`

Owns historical human and agent actions, files changed, claimed outcomes, repairs, and corrections.

Historical entries do not define current task scope.

### Pull request

Owns the proposed change, changed files, acceptance-criterion evidence, check results and their coverage, known risks, self-review, the exact commit reviewed, and the proposed repository state after merge.

## Source precedence

When operating instructions conflict, use this order:

1. Active human-authored work request.
2. Current `repo_control.md`.
3. Current `AGENTS.md`.
4. Current architecture and product documentation.
5. Tests and current implementation behaviour.
6. Historical `agent_record.md` entries.
7. Agent inference.

Precedence determines which instruction governs action. It does not make an incorrect factual statement true.

A material conflict capable of changing implementation is a stop condition.

## Uncertainty reporting

Every work request and pull request must identify material uncertainty when it can change implementation or review.

### Assumptions

Information temporarily treated as true because the repository does not establish it.

### Unknowns

Missing information that could change the correct implementation.

### Conflicts

Authoritative repository sources that provide incompatible instructions or facts.

### External dependencies

Systems, repositories, people, policies, or environments outside the current repository.

The agent does not need to classify every sentence. Material uncertainty must be surfaced rather than hidden behind confident implementation.

## Enforcement states

Every governance constraint has one of three states.

### Declared

The constraint is written down. No automated enforcement is claimed. All constraints default to Declared.

### Checked

A named human or tool evaluated the constraint for an exact commit. The evidence must identify the exact commit, who or what performed the check, the result, what the check proves, and what the check does not prove.

### Required

An external repository or platform rule prevents merging unless the named check succeeds. This state requires evidence from the repository host or another external enforcement system.

No constraint may claim Checked or Required without corresponding evidence.

## Human Blueprint Activation

When no active step exists, only the human may create a bounded governance activation change.

That activation change may:

1. Define one active step.
2. Define planned future steps.
3. Update governance state.
4. Append a truthful human record entry.

That activation change may not implement the newly activated step.

Agent implementation begins only after the activation state is authoritative and a matching human-authored work request exists.

## Mechanical repository orchestration

The protocol distinguishes human scope authority from mechanical repository orchestration.

An agent may create or populate an issue only for an already human-approved active blueprint step by copying its frozen scope without adding, removing, or inventing requirements.

An agent may create a branch, implement the active issue, append its record, open a pull request, self-review, request review, and ask the human to merge.

An agent may not merge, activate an undefined step, invent scope, or close work by falsely claiming a merge occurred.

After human merge activates an already planned step, an agent may mechanically create the matching issue from that frozen step.

## Stop conditions

The agent must stop implementation and report the blocker when:

1. No active step exists.
2. No matching human-authored work request exists.
3. Material repository sources conflict.
4. Missing information could change the correct implementation.
5. Required external context is unavailable.
6. The work cannot be completed inside the allowed file scope.
7. Acceptance criteria cannot all be satisfied together.
8. The requested change would weaken human authority without explicit authorisation.

The correct result is Quarantine or human resolution, not creative guessing.

## External pilot

The external pilot tests this v0.1 contract in a separate repository through three bounded work cycles. At least one cycle must begin with a fresh agent that has no access to the original planning conversation.

The pilot records orientation, scope compliance, restraint, evidence quality, clarification requests, human interventions, review findings, continuity, useful protocol elements, and unnecessary ceremony.

No next protocol phase is defined until human review of the completed pilot.

## Reserved capabilities

Until pilot evidence justifies them, the protocol does not plan mandatory host enforcement, external witnesses, formal evidence receipts, advanced provenance, automated acceptance-criterion interpretation, review orchestration, installation tooling, dashboards, signed governance records, or independent transparency logs.
