# Phase II Monorepo - Full-Stack Application

A full-stack application structured as a monorepo with separate frontend and backend components. This Phase II transition introduces Next.js for the frontend and FastAPI for the backend while maintaining the Phase I backend functionality during the migration.

## Structure

This repository is organized as a monorepo with the following main components:

### Directories
- `frontend/` - Next.js application and related files
- `backend/` - FastAPI application and related files
- `specs/` - All specifications organized by category
- `.spec-kit/` - Configuration for the Spec-Kit tools
- `history/` - Historical records and documentation

### Specification Categories
- `specs/features/` - Feature specifications
- `specs/api/` - API specifications
- `specs/database/` - Database specifications
- `specs/ui/` - UI specifications
- `specs/overview.md` - Overall specification overview

## Phase I Backend Functionality

The original Phase I in-memory console application is preserved in the `backend/` directory:
- Add tasks with title and description
- View all tasks in a table format
- Update existing tasks
- Mark tasks as complete
- Delete tasks
- In-memory storage (data lost on exit)

## Requirements

### Backend
- Python 3.13+
- `rich` library for console output

### Frontend
- Node.js (version TBD)
- Next.js framework
- TypeScript

## Migration Status

This is a work-in-progress migration from Phase I to Phase II. Currently:
- Directory structure has been reorganized
- Backend code has been moved to the backend/ directory
- Configuration files have been created for different contexts
- Specification files have been reorganized

## Running the Application

### Backend (Phase I functionality)
From the backend directory:
```bash
cd backend
uv run python -m src.main
```

## Architecture

The monorepo follows a modular architecture with clear separation of concerns:
- **Frontend**: Next.js application in `frontend/` directory
- **Backend**: FastAPI application in `backend/` directory
- **Specifications**: Organized by category in `specs/` directory
- **Configuration**: Context-specific guidelines in `CLAUDE.md` files