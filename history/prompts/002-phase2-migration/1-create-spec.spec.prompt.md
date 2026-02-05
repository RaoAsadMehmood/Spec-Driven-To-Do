---
id: 1
title: create-spec
stage: spec
date: 2026-02-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: phase2-migration
branch: 002-phase2-migration
user: user
command: /sp.specify
labels: [spec, monorepo, migration, structure, organization]
links:
  spec: ../../specs/02_phase2_migration.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/02_phase2_migration.md
tests:
 - none
---

## Prompt

```
Context: Phase II Kickoff - Transition to Monorepo & Spec-Kit Plus.

Create a new specification file: `specs/02_phase2_migration.md`.

**Title:** Phase II - Monorepo & Spec-Kit Migration

**Objective:**
Restructure the current flat repository into a Spec-Kit compliant Monorepo to support Full-Stack development.

**Requirements:**
1.  **Directory Structure:**
    - Create `frontend/` (Next.js context).
    - Create `backend/` (FastAPI context).
    - Create `.spec-kit/` (Config context).
    - Reorganize `specs/` into subdirectories: `features/`, `api/`, `database/`, `ui/`, `overview.md`.
2.  **Code Migration:**
    - Move existing Phase I Python code (`src/` and `tests/`) into `backend/`.
    - Ensure `backend/` has its own `pyproject.toml` (copy from root if needed).
3.  **Constitution (CLAUDE.md):**
    - Overwrite root `CLAUDE.md` with the "Monorepo Root" content provided in Phase II docs.
    - Create `frontend/CLAUDE.md` with "Frontend Guidelines".
    - Create `backend/CLAUDE.md` with "Backend Guidelines".
4.  **Spec-Kit Config:**
    - Create `.spec-kit/config.yaml` with the defined structure.

**Constraints:**
- Do NOT delete the Phase I logic; preserve it inside `backend/` for reference.
- Do NOT start implementing Next.js or FastAPI logic yet; this phase is strictly for **File Organization**.
```

## Response snapshot

Created the specification file for Phase II - Monorepo & Spec-Kit Migration. The specification includes:

- Three prioritized user stories covering repository restructuring, configuration management, and spec organization
- Ten functional requirements (FR-001 to FR-010) detailing all required changes
- Technical architecture section with directory structure and import constraints
- Key entities definition for the monorepo structure
- Five measurable success outcomes (SC-001 to SC-005)

The specification follows the template structure and addresses all requirements from the prompt including directory creation, code migration, configuration files, and organization constraints.

## Outcome

- ✅ Impact: Created comprehensive specification for monorepo migration
- 🧪 Tests: none required for specification creation
- 📁 Files: Created specs/02_phase2_migration.md
- 🔁 Next prompts: Ready for implementation planning with /sp.plan
- 🧠 Reflection: Specification covers all requirements with proper user story prioritization

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed with implementation planning