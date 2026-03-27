import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Frequency


def test_task_completion():
    """Calling complete() should change is_completed from False to True."""
    task = Task(
        task_id="t1",
        name="Morning Walk",
        description="Walk around the block",
        category="walk",
        duration=30,
        priority=3,
        frequency=Frequency.DAILY,
    )

    assert task.is_completed == False   # starts incomplete
    task.complete()
    assert task.is_completed == True    # now marked done


def test_task_addition():
    """Adding a task to a Pet should increase its task count by 1."""
    pet = Pet(name="Buddy", species="Dog", age=3)

    assert len(pet.get_tasks()) == 0    # starts with no tasks

    task = Task(
        task_id="t2",
        name="Breakfast",
        description="Morning kibble",
        category="feed",
        duration=10,
        priority=3,
        frequency=Frequency.DAILY,
    )
    pet.add_task(task)

    assert len(pet.get_tasks()) == 1    # now has one task
