# Data Model: Phase I - In-Memory Python Console App

**Feature**: 001-console-todo-app
**Date**: 2026-02-05

## Entity Definitions

### Task Entity

**Description**: Represents a to-do item with core information needed for user task management

**Fields**:
- `id: int` - Unique identifier automatically assigned when task is created (sequential)
- `title: str` - User-defined title of the task
- `description: str` - Detailed description of the task
- `status: str` - Current status of the task (Enum: PENDING, COMPLETED)
- `created_at: datetime` - Timestamp when the task was created

**Validation Rules**:
- `id` must be positive integer
- `title` must not be empty/whitespace only
- `description` can be empty
- `status` must be one of the allowed values (PENDING, COMPLETED)
- `created_at` must be a valid datetime

**State Transitions**:
- Initial state: PENDING
- From PENDING → COMPLETED (when user marks task complete)
- From COMPLETED → PENDING (when user marks task incomplete, if implemented)
- Task is deleted from system when deleted (no soft-delete in Phase I)

### Task List (Collection)

**Description**: In-memory collection of Task entities managed during application runtime

**Operations**:
- Add new Task entity to collection
- Retrieve all Task entities from collection
- Find Task entity by ID
- Update Task entity by ID
- Delete Task entity by ID

## Relationships

### Task Relationships
- No direct relationships with other entities (Phase I constraint)
- Belongs to single-user context (no sharing in Phase I)

## Constraints

### Phase I Specific Constraints
- **In-Memory Storage**: Data is lost when application exits (Phase I requirement)
- **Single-User**: No multi-user support in Phase I
- **No Persistence**: No file or database storage in Phase I
- **Sequential IDs**: Auto-generated as monotonically increasing integers

### Data Integrity
- Each Task must have a unique ID within the collection
- IDs are not reused after deletion
- Empty titles are rejected during creation/update
- Descriptions can be modified after creation
- Status can only be changed through specific operations

## API Contract Elements

### Expected Operations
- CREATE: Add new Task with title and description (returns new Task with assigned ID)
- READ: Retrieve all Tasks or specific Task by ID
- UPDATE: Modify Task title, description, or status by ID
- DELETE: Remove Task by ID