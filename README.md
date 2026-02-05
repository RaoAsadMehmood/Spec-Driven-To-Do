# Phase I - In-Memory Python Console App

A CLI-based Todo Application that manages tasks in memory. This is the foundational phase focusing on architectural purity, clean code, and separation of concerns before introducing persistence or AI.

## Features

- Add tasks with title and description
- View all tasks in a table format
- Update existing tasks
- Mark tasks as complete
- Delete tasks
- In-memory storage (data lost on exit)

## Requirements

- Python 3.13+
- `rich` library for console output

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   # or
   pip install rich
   ```

## Usage

Run the application directly with uv:
```bash
uv run src/main.py
```

Or install and run:
```bash
uv pip install -e .
todo-app
```

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data model
├── services/
│   └── todo_service.py  # Business logic for task management
├── ui/
│   └── console_ui.py    # Rich-based console user interface
└── main.py              # Application entry point
```

## Architecture

The application follows a modular architecture with separate concerns:
- **Models**: Data structures and validation
- **Services**: Business logic and data operations
- **UI**: User interface and interaction
- **Main**: Application flow and orchestration