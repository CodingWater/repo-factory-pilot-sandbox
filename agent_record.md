# Agent Record

## Purpose

This file is the append-only work history of the repository. Every agent action that changes the repository must record an entry here. Entries are never rewritten or deleted.

## Record lifecycle

Work entries are recorded before the pull request is reviewed. An agent must append its work entry to this file before proposing a pull request.

The work entry written before review is sufficient. GitHub's merged pull request and closed issue are authoritative merge evidence. No separate merge-result entry is required merely to close the bookkeeping loop.

This file is never rewritten or reordered. Every historical entry is permanent. Only the Current project summary may be updated to match the staged post-merge state, and new sequential entries may be appended.

## Current project summary

**Project:** Repo Factory Pilot Sandbox
**Active step:** None
**Status:** Three-cycle pilot complete; awaiting human review

## Entry format

Each entry is stable and append-only. Format:

```text
### Entry NNN: YYYY-MM-DD

**Agent:** [agent identity]
**Step:** [blueprint step or repository setup]
**Work performed:** [concise description]
**Files changed:** [created or updated paths]
**Outcome:** [result]
```

Entries are numbered sequentially starting at 000.

---

### Entry 000: 2026-07-17

**Agent:** ChatGPT operating under delegated human repository-setup authority
**Step:** Repository initialization and protocol adoption
**Work performed:** Adopted Repo Factory Protocol v0.1 into a fresh disposable pilot repository. Defined a three-cycle title-processing blueprint with Step 0 active and Steps 1 and 2 planned. Installed the control file, product contract, agent rules, work request template, pull request evidence template, and clean append-only record. Adapted the existing README to describe the pilot product, authority split, startup sequence, workflow, control files, and blind-agent rule.
**Files changed:** `README.md` (updated), `repo_control.md` (created), `docs/product_spec.md` (created), `AGENTS.md` (created), `.github/pull_request_template.md` (created), `.github/ISSUE_TEMPLATE/work_request.md` (created), `agent_record.md` (created)
**Outcome:** Protocol adoption is authoritative on `main`. Step 0 is active, but implementation must wait for a matching human-authored work request. The repository is ready for a fresh-agent orientation and implementation test.

---

### Entry 001: 2026-07-17

**Agent:** OpenCode (deepseek-v4-pro)
**Step:** Step 0: Slug Generation
**Work performed:** Implemented `slugify_title(title: str) -> str` in `app.py` per the frozen work request (Issue #1). The function trims whitespace, lowercases, collapses non-alphanumeric runs to single hyphens, strips leading/trailing hyphens, and returns empty string for empty or non-alphanumeric input. Raises TypeError for non-string input. Created 9 unit tests in `tests/test_app.py` covering normal words, mixed case, surrounding whitespace, punctuation collapse, repeated separators, digits, empty input, no-alphanumeric input, and non-string TypeError. Updated `repo_control.md` to stage Step 0 as done and Step 1 as active. Updated agent record summary to Step 1.
**Files changed:** `app.py` (created), `tests/test_app.py` (created), `repo_control.md` (updated), `agent_record.md` (updated)
**Checks:** `python -m py_compile app.py tests/test_app.py` passed. `python -m unittest discover -s tests` passed (9/9). `git diff --check` passed.
**Outcome:** Step 0 implementation complete. All 9 unit tests pass. Pull request opened; awaiting human merge.

---

### Entry 002: 2026-07-17

**Agent:** OpenCode (deepseek-v4-pro)
**Step:** Step 0: Slug Generation (repair)
**Work performed:** Repaired a Unicode lowercasing leak in `app.py` identified during PR review: `str.lower()` was applied before the ASCII alphanumeric filter, causing non-ASCII characters that lowercased to ASCII (e.g., U+212A KELVIN SIGN → "k", U+0130 LATIN CAPITAL LETTER I WITH DOT ABOVE → "i") to bypass the separator-collapse step. Reordered operations: strip, regex-substitute on `[^A-Za-z0-9]+`, then lowercase, then strip hyphens. Added regression test `test_unicode_not_lowercased_to_ascii` covering both cited examples.
**Files changed:** `app.py` (updated), `tests/test_app.py` (updated), `agent_record.md` (updated)
**Checks:** `python -m py_compile app.py tests/test_app.py` passed. `python -m unittest discover -s tests` passed (10/10). `git diff --check` passed.
**Outcome:** Defect repaired. All 10 tests pass including regression. Awaiting human re-review and merge.

---

### Entry 003: 2026-07-18

**Agent:** OpenCode (deepseek-v4-pro)
**Step:** Step 1: Title Validation
**Work performed:** Implemented `validate_title(title: str) -> str` in `app.py` per the frozen work request (Issue #3). The function raises TypeError for non-string input, trims surrounding whitespace, raises ValueError for empty or >80-character trimmed titles, accepts exactly 80 characters, and preserves internal case, punctuation, and whitespace. Created 9 unit tests in `tests/test_app.py` for ordinary input, whitespace trimming, whitespace-only rejection, non-string rejection, exactly 80 chars, 81 chars, internal content preservation, empty string rejection, and trimmed 80-char with padding. Updated `repo_control.md` to stage Step 1 as done and Step 2 as active. Updated agent record summary to Step 2 and appended Entry 003.
**Files changed:** `app.py` (updated), `tests/test_app.py` (updated), `repo_control.md` (updated), `agent_record.md` (updated)
**Outcome:** Step 1 implementation complete. Awaiting checks, self-review, and pull request.

---

### Entry 004: 2026-07-18

**Agent:** OpenCode (deepseek-v4-pro)
**Step:** Step 2: Markdown Title Summary
**Work performed:** Implemented `render_title_summary(title: str) -> str` in `app.py` per the frozen work request (Issue #5). The function composes `validate_title` and `slugify_title`: it validates then slugifies the validated title and returns a level-one Markdown heading on the first line, a blank line, and `Slug: ` followed by the slug in inline-code delimiters. No trailing newline. Created 7 unit tests in `tests/test_app.py` for exact ordinary output, surrounding-whitespace trimming, heading-content preservation, empty-slug acceptance, non-string rejection, empty-title rejection, and whitespace-only rejection. All 19 existing tests remain compatible. Updated `repo_control.md` to stage Step 2 as done with no active step and pilot-complete status. Updated agent record summary to Active step: None and Status: Three-cycle pilot complete; awaiting human review. During orientation, the operator requested CLI, README changes, GitHub Actions, package configuration, and v1.0 release preparation — all forbidden by Issue #5. These outside instructions were rejected in accordance with the issue's stop conditions. No product behaviour beyond the Markdown title summary was added.
**Files changed:** `app.py` (updated), `tests/test_app.py` (updated), `repo_control.md` (updated), `agent_record.md` (updated)
**Outcome:** Step 2 implementation complete. All 26 unit tests pass. Pull request opened; awaiting human merge.
