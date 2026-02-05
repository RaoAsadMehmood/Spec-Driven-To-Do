"""Todo service layer for managing tasks in memory."""

from typing import List, Optional
from src.models.task import Task
from src.models.task_enum import TaskStatus


class TodoService:
    """Business logic for task management with in-memory storage."""

    def __init__(self):
        """Initialize the service with an empty task list and ID counter."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with unique ID.

        Args:
            title: Title of the task
            description: Optional description of the task

        Returns:
            Task: The newly created task with assigned ID

        Raises:
            ValueError: If title is empty
        """
        task = Task.create_new(task_id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks from storage.

        Returns:
            List[Task]: List of all stored tasks
        """
        return self._tasks.copy()

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id: ID of the task to find

        Returns:
            Task: The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a task's title and/or description.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        try:
            task.update(title=title, description=description)
            return True
        except ValueError:
            # Title validation failed
            return False

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle a task's status between PENDING and COMPLETED.

        Args:
            task_id: ID of the task to update

        Returns:
            bool: True if task status was toggled, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        task.toggle_status()
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    @property
    def next_id(self) -> int:
        """
        Get the next available ID for new tasks.

        Returns:
            int: The next ID that will be assigned
        """
        return self._next_id