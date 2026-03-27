from pawpal_system import Task, Pet, Owner, Scheduler, TimeOfDay, Frequency

# --- Setup Owner ---
owner = Owner(name="Alex", available_time=90)  # 90 minutes available today

# --- Setup Pets ---
buddy = Pet(name="Buddy", species="Dog", age=3)
whiskers = Pet(name="Whiskers", species="Cat", age=5, special_needs=["medication"])

owner.add_pet(buddy)
owner.add_pet(whiskers)

# --- Add Tasks to Buddy (Dog) ---
buddy.add_task(Task(
    task_id="t1",
    name="Morning Walk",
    description="30-minute walk around the neighborhood",
    category="walk",
    duration=30,
    priority=3,
    frequency=Frequency.DAILY,
    preferred_time=TimeOfDay.MORNING,
))

buddy.add_task(Task(
    task_id="t2",
    name="Breakfast",
    description="Feed Buddy his morning kibble",
    category="feed",
    duration=10,
    priority=3,
    frequency=Frequency.DAILY,
    preferred_time=TimeOfDay.MORNING,
))

buddy.add_task(Task(
    task_id="t3",
    name="Fetch & Play",
    description="Backyard fetch session for enrichment",
    category="enrichment",
    duration=20,
    priority=2,
    frequency=Frequency.DAILY,
    preferred_time=TimeOfDay.AFTERNOON,
))

# --- Add Tasks to Whiskers (Cat) ---
whiskers.add_task(Task(
    task_id="t4",
    name="Medication",
    description="Administer daily heart medication with food",
    category="medication",
    duration=5,
    priority=3,
    frequency=Frequency.DAILY,
    preferred_time=TimeOfDay.MORNING,
))

whiskers.add_task(Task(
    task_id="t5",
    name="Brushing",
    description="Weekly coat brushing to reduce shedding",
    category="grooming",
    duration=15,
    priority=1,
    frequency=Frequency.WEEKLY,
    preferred_time=TimeOfDay.EVENING,
))

# --- Print Pet Profiles ---
print("=== Pets ===")
for pet in owner.pets:
    print(f"  {pet.get_profile()}")

# --- Run Scheduler ---
scheduler = Scheduler(owner)
scheduler.generate_plan()
scheduler.display_plan()
