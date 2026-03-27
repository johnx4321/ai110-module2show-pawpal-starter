from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pet:
    name: str
    species: str
    age: int
    special_needs: list[str] = field(default_factory=list)

    def get_profile(self) -> str:
        pass


@dataclass
class Task:
    task_id: str
    name: str
    category: str       # walk, feed, medication, grooming, enrichment
    duration: int       # minutes
    priority: int       # 1 (low) to 3 (high)
    preferred_time: Optional[str] = None  # morning, afternoon, evening

    def to_dict(self) -> dict:
        pass


class Owner:
    def __init__(self, name: str, available_time: int, preferences: dict = None):
        self.name = name
        self.available_time = available_time  # minutes per day
        self.preferences = preferences or {}
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.tasks: list[Task] = []
        self.scheduled_tasks: list[Task] = []
        self.unscheduled_tasks: list[Task] = []
        self.explanations: dict[str, str] = {}  # task_id -> reason

    def generate_plan(self) -> None:
        pass

    def prioritize_tasks(self) -> list[Task]:
        pass

    def explain_plan(self) -> dict[str, str]:
        pass

    def display_plan(self) -> None:
        pass
