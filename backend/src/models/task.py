"""Task data model for the todo application."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from .task_enum import TaskStatus


@dataclass
class Task:
    """Represents a to-do item with core information needed for user task management."""

    id: int
    title: str
    description: str
    status: TaskStatus
    created_at: datetime

    def __post_init__(self):
        """Validate task attributes after initialization."""
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if not isinstance(self.status, TaskStatus):
            raise ValueError(f"Status must be a valid TaskStatus, got {self.status}")

    @classmethod
    def create_new(cls, task_id: int, title: str, description: str = "") -> "Task":
        """
        Create a new Task instance with default status PENDING.

        Args:
            task_id: Unique identifier for the task
            title: Title of the task (cannot be empty)
            description: Optional description of the task

        Returns:
            Task: A new Task instance

        Raises:
            ValueError: If title is empty
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        return cls(
            id=task_id,
            title=title.strip(),
            description=description.strip(),
            status=TaskStatus.PENDING,
            created_at=datetime.now(),
        )

    def update(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
        """
        Update task title and/or description.

        Args:
            title: New title (optional)
            description: New description (optional)

        Raises:
            ValueError: If title is provided but is empty
        """
        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            self.title = title.strip()

        if description is not None:
            self.description = description.strip()

    def toggle_status(self) -> None:
        """Toggle the task status between PENDING and COMPLETED."""
        if self.status == TaskStatus.PENDING:
            self.status = TaskStatus.COMPLETED
        else:
            self.status = TaskStatus.PENDING