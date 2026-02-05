# CLI Interface Contract: Phase I - In-Memory Python Console App

**Feature**: 001-console-todo-app
**Date**: 2026-02-05

## Overview

This document defines the command-line interface contract for the console-based todo application. The interface follows a menu-driven pattern with numbered options corresponding to different operations.

## Menu Interface

### Main Menu Options
The application presents a main menu with the following numbered options:

1. **Add Task** - Add a new task to the todo list
2. **List Tasks** - Display all tasks in a table format
3. **Update Task** - Modify an existing task's title or description
4. **Mark Complete** - Toggle a task's status to/from completed
5. **Delete Task** - Remove a task from the list
6. **Exit** - Close the application

## Operation Contracts

### 1. Add Task
**Input**:
- Prompt for "Task Title:" (string input)
- Prompt for "Task Description:" (string input)

**Processing**:
- Validate title is not empty
- Generate unique sequential ID
- Set initial status to "PENDING"
- Set creation timestamp
- Add to in-memory task collection

**Output**:
- Success message: "Task added successfully with ID: [ID]"
- Or error message if title is empty

### 2. List Tasks
**Input**: None required (selected from menu)

**Processing**:
- Retrieve all tasks from in-memory collection
- Format as table using `rich` library

**Output**:
- Table display with columns: ID, Title, Description, Status, Created At
- Message "No tasks found" if collection is empty

### 3. Update Task
**Input**:
- Prompt for "Task ID:" (integer input)
- Prompt for "New Title:" (string input)
- Prompt for "New Description:" (string input)

**Processing**:
- Verify task with given ID exists
- Update title and/or description
- Leave other fields unchanged

**Output**:
- Success message: "Task [ID] updated successfully"
- Error message if task ID doesn't exist

### 4. Mark Complete
**Input**:
- Prompt for "Task ID:" (integer input)

**Processing**:
- Verify task with given ID exists
- Toggle status between "PENDING" and "COMPLETED"

**Output**:
- Success message: "Task [ID] marked as [COMPLETED/PENDING]"
- Error message if task ID doesn't exist

### 5. Delete Task
**Input**:
- Prompt for "Task ID:" (integer input)

**Processing**:
- Verify task with given ID exists
- Remove from in-memory collection

**Output**:
- Success message: "Task [ID] deleted successfully"
- Error message if task ID doesn't exist

### 6. Exit
**Input**: None required

**Processing**:
- Terminate the main application loop
- Allow graceful shutdown

**Output**:
- End program execution

## Error Handling Contract

### Expected Error Conditions
1. **Invalid Task ID**: Input that doesn't match an existing task
   - Response: "Error: Task with ID [ID] not found"

2. **Empty Title**: Attempt to create/update with empty title
   - Response: "Error: Task title cannot be empty"

3. **Invalid Input**: Non-numeric input when numeric expected
   - Response: "Error: Please enter a valid number"

### Error Handling Requirements
- No application crashes under any input condition
- Clear, user-friendly error messages
- Return to main menu after displaying error
- Preserve data integrity despite invalid inputs

## UI Display Contract

### Table Format
Tasks will be displayed in a rich table with:
- Column headers: ID, Title, Description, Status, Created At
- Proper column alignment
- Color-coded status indicators (PENDING: yellow, COMPLETED: green)
- Scrollable display for long lists (via rich library)

### Input Prompts
- Clear labeling of required inputs
- Input validation before processing
- Confirmation for destructive operations (delete)

## Type Contract

All function interfaces must include type hints following Python typing conventions:
- `task_id: int`
- `title: str`
- `description: str`
- `status: str`
- Return types appropriately annotated