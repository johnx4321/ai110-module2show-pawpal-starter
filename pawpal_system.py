from dataclasses import dataclass
from typing import Optional
from enum import Enum


class TimeOfDay(Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"


class Frequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    AS_NEEDED = "as_needed"


@dataclass
class Task:
    task_id: str
    name: str
    description: str
    category: str               # walk, feed, medication, grooming, enrichment
    duration: int               # minutes
    priority: int               # 1 (low) to 3 (high)
    frequency: Frequency = Frequency.DAILY
    preferred_time: Optional[TimeOfDay] = None
    is_completed: bool = False

    def complete(self) -> None:
        """Mark this task as done."""
        self.is_completed = True

    def reset(self) -> None:
        """Reset completion status (e.g. for a new day)."""
        self.is_completed = False

    def to_dict(self) -> dict:
        """Serialize task to a dictionary for display or storage."""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "duration": self.duration,
            "priority": self.priority,
            "frequency": self.frequency.value,
            "preferred_time": self.preferred_time.value if self.preferred_time else None,
            "is_completed": self.is_completed,
        }


class Pet:
    def __init__(self, name: str, species: str, age: int, special_needs: list[str] = None):
        self.name = name
        self.species = species
        self.age = age
        self.special_needs = special_needs or []
        self.tasks: list[Task] = []         # tasks belong to the pet

    def add_task(self, task: Task) -> None:
        """Add a care task for this pet."""
        self.tasks.append(task)

    def remove_task(self, task_id: str) -> None:
        """Remove a task by its ID."""
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def get_tasks(self) -> list[Task]:
        """Return all tasks for this pet."""
        return self.tasks

    def get_profile(self) -> str:
        """Return a readable summary of this pet."""
        needs = ", ".join(self.special_needs) if self.special_needs else "none"
        return f"{self.name} ({self.species}, age {self.age}) — special needs: {needs}"


class Owner:
    def __init__(self, name: str, available_time: int, preferences: dict = None):
        self.name = name
        self.available_time = available_time    # total minutes available per day
        self.preferences = preferences or {}
        self.pets: list[Pet] = []               # owner manages multiple pets

    def add_pet(self, pet: Pet) -> None:
        """Register a pet under this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet by name."""
        self.pets = [p for p in self.pets if p.name != pet_name]

    def get_all_tasks(self) -> list[Task]:
        """Collect and return tasks across all pets — entry point for Scheduler."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.scheduled_tasks: list[Task] = []
        self.unscheduled_tasks: list[Task] = []
        self.explanations: dict[str, str] = {}  # task_id -> reason string

    def generate_plan(self) -> None:
        """Main entry point: build the daily plan from the owner's pets' tasks."""
        # reset state so re-runs don't stack
        self.scheduled_tasks = []
        self.unscheduled_tasks = []
        self.explanations = {}

        ordered = self.prioritize_tasks()
        time_remaining = self.owner.available_time

        for task in ordered:
            if task.duration <= time_remaining:
                self.scheduled_tasks.append(task)
                time_remaining -= task.duration
                self.explanations[task.task_id] = (
                    f"Scheduled '{task.name}' ({task.duration} min, priority {task.priority})"
                )
            else:
                self.unscheduled_tasks.append(task)
                self.explanations[task.task_id] = (
                    f"Skipped '{task.name}' — not enough time remaining ({time_remaining} min left)"
                )

    def prioritize_tasks(self) -> list[Task]:
        """
        Retrieve all tasks from the owner's pets and sort them.
        Higher priority first; within same priority, shorter tasks first.
        Completed tasks are excluded.
        """
        # Scheduler reaches tasks via: Scheduler -> Owner -> Pet -> Tasks
        all_tasks = self.owner.get_all_tasks()
        pending = [t for t in all_tasks if not t.is_completed]
        return sorted(pending, key=lambda t: (-t.priority, t.duration))

    def explain_plan(self) -> dict[str, str]:
        """Return the reasoning behind each scheduling decision."""
        return self.explanations

    def display_plan(self) -> None:
        """Print a formatted summary of the daily plan."""
        print(f"\n=== Daily Plan for {self.owner.name} ===")
        print(f"Available time: {self.owner.available_time} min\n")

        print("Scheduled:")
        for task in self.scheduled_tasks:
            print(f"  [{task.preferred_time.value if task.preferred_time else 'anytime'}] "
                  f"{task.name} — {task.duration} min (priority {task.priority})")

        if self.unscheduled_tasks:
            print("\nCould not fit:")
            for task in self.unscheduled_tasks:
                print(f"  {task.name} — {task.duration} min")

        print("\nReasons:")
        for reason in self.explanations.values():
            print(f"  - {reason}")
