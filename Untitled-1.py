
class Task:

    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def to_dict(self):
        
        return {
            "id": self.task_id,
            "description": self.description,
            "completed": self.completed,
        }

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] ({self.task_id}) {self.description}"


class ToDoApp:

    def __init__(self):
        self.tasks = {}     
        self.next_id = 1


    def add_task(self, description):
    
        if not description.strip():
            print("  Error: Task description cannot be empty.")
            return None

        task = Task(self.next_id, description.strip())
        self.tasks[self.next_id] = task
        self.next_id += 1
        print(f"  Task added: {task}")
        return task

    def complete_task(self, task_id):
        """Mark a task as completed."""
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if task.completed:
                print(f"  Task {task_id} is already completed.")
            else:
                task.mark_complete()
                print(f"  Task marked complete: {task}")
        else:
            print(f"  Error: No task found with ID {task_id}.")

    def uncomplete_task(self, task_id):
        """Mark a completed task as incomplete again."""
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if not task.completed:
                print(f"  Task {task_id} is already incomplete.")
            else:
                task.mark_incomplete()
                print(f"  Task marked incomplete: {task}")
        else:
            print(f"  Error: No task found with ID {task_id}.")

    def delete_task(self, task_id):
        """Delete a task by ID."""
        if task_id in self.tasks:
            removed = self.tasks.pop(task_id)
            print(f"  Deleted: {removed}")
        else:
            print(f"  Error: No task found with ID {task_id}.")

    # ── View helpers ──────────────────────────────────────────────────────────

    def view_all(self):
        """Display all tasks."""
        if not self.tasks:
            print("  No tasks yet. Add one!")
            return

        print(f"\n  {'─' * 40}")
        print(f"  {'All Tasks':^40}")
        print(f"  {'─' * 40}")
        for task in self.tasks.values():
            print(f"  {task}")
        print(f"  {'─' * 40}")
        self._print_summary()

    def view_pending(self):
        """Display only incomplete tasks."""
        pending = [t for t in self.tasks.values() if not t.completed]
        if not pending:
            print("  No pending tasks — great job!")
            return

        print(f"\n  {'─' * 40}")
        print(f"  {'Pending Tasks':^40}")
        print(f"  {'─' * 40}")
        for task in pending:
            print(f"  {task}")
        print(f"  {'─' * 40}")

    def view_completed(self):
        """Display only completed tasks."""
        done = [t for t in self.tasks.values() if t.completed]
        if not done:
            print("  No completed tasks yet.")
            return

        print(f"\n  {'─' * 40}")
        print(f"  {'Completed Tasks':^40}")
        print(f"  {'─' * 40}")
        for task in done:
            print(f"  {task}")
        print(f"  {'─' * 40}")

    def _print_summary(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks.values() if t.completed)
        print(f"  Summary: {done}/{total} completed")

    # ── Menu & main loop ──────────────────────────────────────────────────────

    @staticmethod
    def _print_menu():
        print("\n" + "=" * 44)
        print("        📝  TO-DO LIST APPLICATION")
        print("=" * 44)
        print("  1. Add a task")
        print("  2. Mark task as completed")
        print("  3. Mark task as incomplete")
        print("  4. Delete a task")
        print("  5. View all tasks")
        print("  6. View pending tasks")
        print("  7. View completed tasks")
        print("  8. Quit")
        print("=" * 44)

    def _get_task_id(self, prompt="  Enter task ID: "):
        """Prompt for and validate a task ID."""
        try:
            return int(input(prompt))
        except ValueError:
            print("  Error: Please enter a valid number.")
            return None

    def run(self):
        """Main application loop."""
        print("\nWelcome to the To-Do List App!")

        while True:
            self._print_menu()
            choice = input("  Choose an option (1-8): ").strip()

            if choice == "1":
                desc = input("  Enter task description: ")
                self.add_task(desc)

            elif choice == "2":
                task_id = self._get_task_id()
                if task_id is not None:
                    self.complete_task(task_id)

            elif choice == "3":
                task_id = self._get_task_id()
                if task_id is not None:
                    self.uncomplete_task(task_id)

            elif choice == "4":
                task_id = self._get_task_id()
                if task_id is not None:
                    self.delete_task(task_id)

            elif choice == "5":
                self.view_all()

            elif choice == "6":
                self.view_pending()

            elif choice == "7":
                self.view_completed()

            elif choice == "8":
                print("\n  Goodbye! Stay productive. 👋\n")
                break

            else:
                print("  Invalid choice. Please enter a number between 1 and 8.")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = ToDoApp()
    app.run()