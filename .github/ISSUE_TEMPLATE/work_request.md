---
name: Work Request
about: Request agent work bounded to a single blueprint step.
labels: [work-request]
---

## Classification

<!-- Required. Pick exactly one. -->

- [ ] **Build**: implement a blueprint step
- [ ] **Learning**: research, explore, or clarify before building
- [ ] **Containment**: repair, refactor, or fix without new scope

## Exact blueprint step

<!-- Required. Copy the exact step number and title from repo_control.md. -->

## Purpose

<!-- Required. Why is this work needed? What problem does it solve? -->

## Scope

<!-- Required. Concise, bounded description of what the agent must do. -->

## Allowed files

<!-- Required. List every file the agent may create or modify. Use exact paths. -->

## Forbidden changes

<!-- Required. List what the agent must not do. Include no scope expansion, no new dependencies, and no unlisted files. -->

## Frozen acceptance criteria

<!-- Required. Verifiable and frozen unless the human updates this issue. -->

- [ ] Criterion 1
- [ ] Criterion 2

## Evidence and checks

<!-- Required. State the evidence expected before review. For every automated check, require the command, result, what it proves, and what it does not prove. -->

## Material assumptions

<!-- Required. List assumptions that could change implementation, or write "None known." -->

## Material unknowns

<!-- Required. List missing information that could change implementation, or write "None known." -->

## External dependencies

<!-- Required. List relevant systems, repositories, people, policies, or environments outside this repository, or write "None." -->

## Stop conditions

<!-- Required. State when the agent must stop and report rather than guess or expand scope. -->

## Agent record and status updates

<!-- Required. What entry must be appended to agent_record.md? What project summary and step statuses must change? -->

## Human final merge authority

<!-- Do not remove. This is a protocol gate. -->

- [ ] I understand that the human alone merges. The agent must not merge under any circumstance.

## Agent constraints

<!-- Do not remove. These are protocol rules. -->

- [ ] One issue maps to exactly one blueprint step.
- [ ] The agent must use the smallest correct change.
- [ ] The agent must not expand scope beyond this issue.
- [ ] The agent must not merge.
- [ ] Acceptance criteria are frozen unless the human updates this issue.
