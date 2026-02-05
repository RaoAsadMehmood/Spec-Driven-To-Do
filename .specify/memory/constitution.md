<!-- SYNC IMPACT REPORT:
Version change: N/A (initial creation) → 1.0.0
List of modified principles: N/A (new constitution)
Added sections: Core Mandate, Project Evolution, Technology Standards, Operational Constraints, Directory Structure
Removed sections: N/A
Templates requiring updates: ⚠ pending (plan-template.md, spec-template.md, tasks-template.md)
Follow-up TODOs: None
-->
# The Evolution of Todo (Hackathon II) Constitution

## Core Principles

### I. Spec-Driven Development
The Golden Rule: You are strictly PROHIBITED from writing or modifying any source code without an existing, detailed specification file in the `specs/` directory. Role Definition: Product Owner creates requirements, System Architect and Lead Engineer implements based on approved specs. Workflow: Feature request → Specification in `specs/` → Approval refinement → Implementation code only after spec approval.

### II. Project Evolution (The 5 Phases)
This project follows an iterative journey from a console app to a Cloud-Native AI System with 5 distinct phases: Phase I - In-Memory Python Console App (Current Focus); Phase II - Full-Stack (FastAPI, SQLModel, Neon DB, Next.js); Phase III - AI Chatbot (OpenAI Agents SDK, MCP); Phase IV - Local Kubernetes (Docker, Minikube); Phase V - Cloud Native (Kafka, Dapr, DOKS).

### III. Technology Standards (Python 3.13+ Focus)
All development must follow strict Python Type Hints using the `typing` module as mandatory. Google-style Docstrings required for all classes and functions. Modular Architecture: Separate Concerns (Models, Logic, UI/API). Use `uv` as the package manager for Python. Primary languages: Python 3.13+ for backend, TypeScript for future frontend.

### IV. Operational Constraints
Environment must support Windows (WSL 2) and Ubuntu. Persistence strategy: Phase I uses In-Memory ONLY (No databases), Phase II+ uses Postgres/Neon via SQLModel. All features must be verifiable via `pytest` or manual simulation steps provided by the engineer. Strict adherence to the defined phase boundaries.

### V. Directory Structure and Source of Truth
The `specs/` directory is The Source of Truth for all project specifications (Markdown files). Application Source Code goes in `src/` directory. Test suites are organized in `tests/` directory. Architecture diagrams and infrastructure configs are maintained in `blueprints/` directory. All development must respect this structural organization.

### VI. Quality and Verification
All implementations must include comprehensive test coverage with `pytest`. Documentation must be maintained alongside code changes. Type safety must be preserved throughout all phases. Performance considerations must be addressed before implementation. Code reviews are mandatory for all changes.

## Project Evolution Framework

The project follows a structured evolution from Phase I to Phase V with clear boundaries between each phase. Each phase must be completed before moving to the next. Technology stacks are predetermined for each phase and must not be mixed between phases. Phase-specific constraints (like persistence for Phase I) are strictly enforced.

## Development Workflow

The workflow follows a strict sequence: 1) Product Owner requests a feature. 2) System Architect generates/updates a Markdown file in `specs/`. 3) Specifications are refined collaboratively until approved. 4) Only then may implementation code be generated based on the approved specification. This sequence is non-negotiable.

## Governance

This Constitution supersedes all other development practices and guidelines. All development activities must comply with these principles. Amendments to this constitution require explicit documentation and approval process. All Pull Requests and code reviews must verify constitutional compliance. The Golden Rule of spec-first development is absolute and non-negotiable.

**Version**: 1.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05