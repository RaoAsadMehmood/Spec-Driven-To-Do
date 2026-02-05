"""Main application entry point for the todo console application."""

from typing import Optional
from src.ui.console_ui import ConsoleUI
from src.services.todo_service import TodoService


def main() -> None:
    """Main application loop."""
    # Initialize components
    ui = ConsoleUI()
    service = TodoService()

    # Show welcome message
    ui.display_welcome()

    # Main application loop
    while True:
        # Display menu
        ui.display_menu()

        # Get user choice
        choice = ui.get_user_choice()

        # Process user choice
        if choice == 1:
            # Add Task
            title, description = ui.get_task_details()

            if title:  # Only add if title is not empty
                try:
                    task = service.add_task(title, description)
                    ui.display_success(f"Task '{task.title}' added successfully with ID: {task.id}")
                except ValueError as e:
                    ui.display_error(f"Error adding task: {str(e)}")
            else:
                ui.display_info("Task addition cancelled - title cannot be empty.")

        elif choice == 2:
            # List Tasks
            tasks = service.get_all_tasks()
            ui.display_tasks(tasks)

        elif choice == 3:
            # Update Task
            task_id = ui.get_task_id("update")
            if task_id is not None:
                task = service.find_task_by_id(task_id)
                if task:
                    ui.display_info(f"Updating task {task_id}: {task.title}")
                    title, description = ui.get_task_details()

                    # Use existing values if user doesn't want to change them
                    if not title.strip():
                        title = task.title
                    if not description.strip():
                        description = task.description

                    updated = service.update_task(task_id, title, description)
                    if updated:
                        ui.display_success(f"Task {task_id} updated successfully")
                    else:
                        ui.display_error(f"Error updating task {task_id}")
                else:
                    ui.display_error(f"Task with ID {task_id} not found")

        elif choice == 4:
            # Mark Complete
            task_id = ui.get_task_id("mark complete")
            if task_id is not None:
                toggled = service.toggle_task_status(task_id)
                if toggled:
                    task = service.find_task_by_id(task_id)
                    if task:
                        ui.display_success(f"Task {task_id} marked as {task.status.value}")
                else:
                    ui.display_error(f"Task with ID {task_id} not found")

        elif choice == 5:
            # Delete Task
            task_id = ui.get_task_id("delete")
            if task_id is not None:
                deleted = service.delete_task(task_id)
                if deleted:
                    ui.display_success(f"Task {task_id} deleted successfully")
                else:
                    ui.display_error(f"Task with ID {task_id} not found")

        elif choice == 6:
            # Exit
            if ui.confirm_exit():
                ui.display_info("Thank you for using the Todo Application!")
                break
            else:
                continue

        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()