---
id: 1
title: create-constitution
stage: constitution
date: 2026-02-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, spec-driven-development, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
/create constitution.md
# Constitution: The Evolution of Todo (Hackathon II)

## 1. Core Mandate: Spec-Driven Development
- **The Golden Rule:** You are strictly PROHIBITED from writing or modifying any source code without an existing, detailed specification file in the `specs/` directory.
- **Role Definition:** I am the Product Owner. You are the System Architect and Lead Engineer.
- **Workflow:**
  1. I request a feature.
  2. You generate/update a Markdown file in `specs/`.
  3. We refine the spec together until approved.
  4. ONLY THEN do you generate the implementation code.

## 2. Project Evolution (The 5 Phases)
This project is an iterative journey from a console app to a Cloud-Native AI System.
- **Phase I:** In-Memory Python Console App (Current Focus).
- **Phase II:** Full-Stack (FastAPI, SQLModel, Neon DB, Next.js).
- **Phase III:** AI Chatbot (OpenAI Agents SDK, MCP).
- **Phase IV:** Local Kubernetes (Docker, Minikube).
- **Phase V:** Cloud Native (Kafka, Dapr, DOKS).

## 3. Technology Standards
- **Language:** Python 3.13+ (Primary Backend), TypeScript (Future Frontend).
- **Package Manager:** `uv` (for Python).
- **Style Guide:**
  - Strict Python Type Hints (`typing` module) are mandatory.
  - Google-style Docstrings for all classes and functions.
  - Modular Architecture: Separate Concerns (Models, Logic, UI/API).

## 4. Operational Constraints
- **Environment:** Windows (WSL 2) / Ubuntu.
- **Persistence:**
  - Phase I: In-Memory ONLY (No databases).
  - Phase II+: Postgres/Neon via SQLModel.
- **Testing:** All features must be verifiable via `pytest` or manual simulation steps provided by you.

## 5. Directory Structure
- `specs/` : The Source of Truth (Markdown files).
- `src/` : Application Source Code.
- `tests/` : Test suites.
- `blueprints/` : Architecture diagrams and infrastructure configs.

---
**Acknowledgment:**
By reading this, you agree to act as an Intelligent Agent, prioritizing architectural integrity and spec adherence over quick hacks.
```

## Response snapshot

Created the project constitution file with core principles based on the user's requirements. The constitution includes six core principles covering spec-driven development, project evolution phases, technology standards, operational constraints, directory structure, and quality verification. It also includes sections on project evolution framework, development workflow, and governance with version tracking.

## Outcome

- ✅ Impact: Created foundational governance document for spec-driven development
- 🧪 Tests: none required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with comprehensive constitution
- 🔁 Next prompts: Ready for feature specification and implementation
- 🧠 Reflection: Constitution establishes clear development workflow and principles

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin with first feature specification