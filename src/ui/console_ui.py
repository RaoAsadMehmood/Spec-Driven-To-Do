"""Console user interface for the todo application using rich."""

from typing import Optional, Tuple
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
import sys

from src.models.task import Task
from src.services.todo_service import TodoService
from src.models.task_enum import TaskStatus


class ConsoleUI:
    """Rich-based console user interface for the todo application."""

    def __init__(self):
        """Initialize the UI with a rich console."""
        self.console = Console()

    def display_welcome(self) -> None:
        """Display welcome banner and application info."""
        self.console.rule("[bold blue]Welcome to the Todo Application[/bold blue]")
        self.console.print("Manage your tasks efficiently in memory.\n", style="green")
        self.console.print("Data is lost when the application exits (Phase I requirement).\n", style="yellow")

    def display_menu(self) -> None:
        """Display the main menu options."""
        self.console.rule("[bold]Main Menu[/bold]")
        self.console.print("[bold]1.[/bold] Add Task")
        self.console.print("[bold]2.[/bold] List Tasks")
        self.console.print("[bold]3.[/bold] Update Task")
        self.console.print("[bold]4.[/bold] Mark Complete")
        self.console.print("[bold]5.[/bold] Delete Task")
        self.console.print("[bold]6.[/bold] Exit")
        self.console.rule()

    def get_user_choice(self) -> int:
        """
        Prompt user for menu choice.

        Returns:
            int: User's menu choice (1-6)
        """
        try:
            choice = IntPrompt.ask(
                "[bold]Please select an option[/bold]",
                choices=["1", "2", "3", "4", "5", "6"],
                default=6
            )
            return choice
        except KeyboardInterrupt:
            self.console.print("\n[red]Application interrupted. Exiting...[/red]")
            sys.exit(0)
        except Exception:
            self.console.print("[red]Invalid input. Please enter a number between 1-6.[/red]")
            return 6  # Default to exit on invalid input

    def get_task_details(self) -> Tuple[str, str]:
        """
        Prompt user for task title and description.

        Returns:
            Tuple[str, str]: Title and description entered by user
        """
        try:
            title = Prompt.ask("[bold]Enter task title[/bold]")
            description = Prompt.ask("[bold]Enter task description (optional)[/bold]", default="")
            return title.strip(), description.strip()
        except KeyboardInterrupt:
            self.console.print("\n[red]Operation cancelled.[/red]")
            return "", ""

    def display_tasks(self, tasks: list[Task]) -> None:
        """
        Display all tasks in a rich table format.

        Args:
            tasks: List of tasks to display
        """
        if not tasks:
            self.console.print("[yellow]No tasks found.[/yellow]\n")
            return

        table = Table(title="Task List", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Title", min_width=15)
        table.add_column("Description", min_width=20)
        table.add_column("Status", justify="center")
        table.add_column("Created At", justify="center")

        for task in tasks:
            status_text = Text(task.status.value, style="green" if task.status == TaskStatus.COMPLETED else "yellow")
            table.add_row(
                str(task.id),
                task.title,
                task.description or "[italic]No description[/italic]",
                status_text,
                task.created_at.strftime("%Y-%m-%d %H:%M")
            )

        self.console.print(table)
        self.console.print()  # Add space after table

    def get_task_id(self, action: str = "operate on") -> Optional[int]:
        """
        Prompt user for a task ID.

        Args:
            action: Description of what the ID is needed for (e.g., "update", "delete")

        Returns:
            Optional[int]: Task ID entered by user, or None if cancelled
        """
        try:
            task_id = IntPrompt.ask(f"[bold]Enter task ID to {action}[/bold]", default=None)
            return task_id
        except KeyboardInterrupt:
            self.console.print("\n[red]Operation cancelled.[/red]")
            return None
        except Exception:
            self.console.print("[red]Invalid input. Please enter a valid task ID.[/red]")
            return None

    def display_success(self, message: str) -> None:
        """
        Display a success message.

        Args:
            message: Success message to display
        """
        self.console.print(f"[green]{message}[/green]")

    def display_error(self, message: str) -> None:
        """
        Display an error message.

        Args:
            message: Error message to display
        """
        self.console.print(f"[red]{message}[/red]")

    def display_info(self, message: str) -> None:
        """
        Display an informational message.

        Args:
            message: Info message to display
        """
        self.console.print(f"[blue]{message}[/blue]")

    def confirm_exit(self) -> bool:
        """
        Ask user to confirm exit (Phase I: since data is lost, confirm before exit).

        Returns:
            bool: True if user confirms exit, False to continue
        """
        try:
            confirm = Prompt.ask("[bold red]Are you sure you want to exit? All data will be lost![/bold red]",
                                choices=["y", "n"], default="n")
            return confirm.lower() == "y"
        except KeyboardInterrupt:
            return True  # Exit on interrupt