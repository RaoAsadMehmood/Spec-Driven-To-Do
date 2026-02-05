# Quickstart Guide: Phase II - Monorepo & Spec-Kit Migration

**Feature**: 002-phase2-migration
**Date**: 2026-02-05

## Overview

This guide describes the monorepo migration process that transforms the flat repository structure into a well-organized monorepo with separate frontend and backend contexts.

## Prerequisites

- Basic understanding of directory structures
- Git (to maintain history during migration if needed)
- Understanding of the existing repository structure

## Migration Steps

### 1. Repository Restructuring

The migration involves reorganizing the repository into a monorepo structure:

```
Before:
├── src/
├── tests/
├── pyproject.toml
├── CLAUDE.md
├── specs/
└── ...

After:
├── frontend/
│   ├── CLAUDE.md
│   └── ...
├── backend/
│   ├── CLAUDE.md
│   ├── pyproject.toml
│   ├── src/
│   └── tests/
├── specs/
│   ├── features/
│   ├── api/
│   ├── database/
│   ├── ui/
│   └── overview.md
├── .spec-kit/
│   └── config.yaml
├── CLAUDE.md (root)
└── ...
```

### 2. Directory Creation

Creates the following directories:
- `frontend/` - For Next.js application
- `backend/` - For FastAPI application
- `.spec-kit/` - For Spec-Kit configuration
- Subdirectories in `specs/` - For organized specifications

### 3. Code Migration

Moves existing Phase I code to appropriate locations:
- `src/` → `backend/src/`
- `tests/` → `backend/tests/`
- `pyproject.toml` → `backend/pyproject.toml`

### 4. Configuration Setup

Sets up governance files:
- Root `CLAUDE.md` - Monorepo guidelines
- `frontend/CLAUDE.md` - Frontend guidelines
- `backend/CLAUDE.md` - Backend guidelines
- `.spec-kit/config.yaml` - Configuration file

### 5. Specification Reorganization

Reorganizes specifications into thematic categories:
- `specs/features/` - Feature specifications
- `specs/api/` - API specifications
- `specs/database/` - Database specifications
- `specs/ui/` - UI specifications
- `specs/overview.md` - Overall specification overview

## Verification

After migration, verify:
1. All existing functionality remains intact in `backend/`
2. New directory structure is properly organized
3. All CLAUDE.md files exist with appropriate content
4. Specification files are properly organized
5. The monorepo structure supports the intended development workflow