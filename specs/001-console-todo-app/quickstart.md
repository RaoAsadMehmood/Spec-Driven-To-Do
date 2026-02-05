# Quickstart Guide: Phase I - In-Memory Python Console App

**Feature**: 001-console-todo-app
**Date**: 2026-02-05

## Prerequisites

- Python 3.13+ installed
- `uv` package manager installed

## Setup Instructions

### 1. Clone or Initialize Repository
```bash
# Navigate to your project directory
cd your-project-directory
```

### 2. Install Dependencies
```bash
# Install uv if not already installed
pip install uv

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install project dependencies (rich library)
uv pip install rich pytest
```

### 3. Project Structure
After implementation, your project structure should look like:
```
src/
├── models/
│   └── task.py
├── services/
│   └── todo_service.py
├── ui/
│   └── console_ui.py
└── main.py

tests/
├── unit/
└── integration/
```

## Running the Application

### 1. Execute the Application
```bash
cd src
python main.py
```

### 2. Use the Application
The application will present a menu with the following options:
- [1] Add - Add a new task
- [2] List - View all tasks
- [3] Update - Modify an existing task
- [4] Complete - Mark a task as complete
- [5] Delete - Remove a task
- [6] Exit - Quit the application

## Development Commands

### Run Tests
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src
```

### Type Checking
```bash
# Install mypy
uv pip install mypy

# Run type checking
mypy src/
```

## Sample Usage Session

1. Start the application: `python src/main.py`
2. Choose option 1 to add a task: Enter title and description
3. Choose option 2 to view tasks: See all tasks in table format
4. Choose option 4 to mark a task complete: Enter task ID
5. Choose option 6 to exit

## Troubleshooting

- **Import errors**: Ensure `rich` library is installed: `uv pip install rich`
- **Permission errors**: Activate virtual environment before running
- **Missing modules**: Ensure all source files are in correct directories