"""Task status enumeration for the todo application."""

from enum import Enum


class TaskStatus(str, Enum):
    """Enumeration of possible task statuses."""

    PENDING = "PENDING"
    COMPLETED = "COMPLETED"