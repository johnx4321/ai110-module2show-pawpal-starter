import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler, TimeOfDay, Frequency

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# Initialize owner and pets in session state (persist across reruns)
if 'owner' not in st.session_state:
    # Try to load from JSON file first
    loaded_owner = Owner.load_from_json("data.json")

    if loaded_owner:
        st.session_state.owner = loaded_owner
    else:
        # Create default owner if no saved data
        st.session_state.owner = Owner(name="Jordan", available_time=120)
        buddy = Pet(name="Mochi", species="cat", age=3)
        st.session_state.owner.add_pet(buddy)

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Pet & Owner Details")
col1, col2, col3 = st.columns(3)
with col1:
    owner = st.session_state.owner
    st.write(f"**Owner:** {owner.name}")
with col2:
    st.write(f"**Available time:** {owner.available_time} min/day")
with col3:
    st.write(f"**Pets:** {len(owner.pets)}")

st.divider()

st.subheader("Add Care Tasks")
st.caption("Create tasks for your pets. They will be scheduled based on priority and duration.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: {1: "low", 2: "medium", 3: "high"}[x], index=2)

col1, col2, col3 = st.columns(3)
with col1:
    task_desc = st.text_input("Description", value="Daily exercise")
with col2:
    category = st.selectbox("Category", ["walk", "feed", "medication", "grooming", "enrichment"])
with col3:
    preferred_time = st.selectbox("Preferred time", [None, "morning", "afternoon", "evening"], format_func=lambda x: x if x else "anytime")

if st.button("Add task"):
    pet = st.session_state.owner.pets[0]  # add to first pet
    task_id = f"task_{len(pet.get_tasks()) + 1}"
    new_task = Task(
        task_id=task_id,
        name=task_title,
        description=task_desc,
        category=category,
        duration=int(duration),
        priority=priority,
        frequency=Frequency.DAILY,
        preferred_time=TimeOfDay[preferred_time.upper()] if preferred_time else None,
    )
    pet.add_task(new_task)
    st.session_state.owner.save_to_json("data.json")  # Save to file
    st.success(f"✓ Added '{task_title}' to {pet.name}")
    st.rerun()

# Display current tasks
if st.session_state.owner.pets[0].get_tasks():
    st.write("**Current tasks:**")
    tasks_data = [
        {
            "Title": t.name,
            "Description": t.description,
            "Duration": f"{t.duration} min",
            "Priority": t.priority,
            "Category": t.category,
            "Time": t.preferred_time.value if t.preferred_time else "anytime",
            "Done": "✓" if t.is_completed else "—"
        }
        for t in st.session_state.owner.pets[0].get_tasks()
    ]
    st.table(tasks_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Generate Schedule")
st.caption("Build your daily plan. The scheduler will fit tasks into your available time.")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner)
    scheduler.generate_plan()
    scheduler.sort_by_time()  # Sort tasks by time of day

    st.success("✓ Schedule generated!")

    st.write(f"**Available time:** {st.session_state.owner.available_time} min")

    # Display scheduling conflicts if any exist
    if scheduler.conflicts:
        st.warning("⚠️ **Scheduling Conflicts Detected**")
        for conflict in scheduler.conflicts:
            st.caption(conflict)
        with st.expander("💡 How to resolve"):
            st.markdown(
                """
                **Conflict detected:** Multiple tasks are scheduled for the same time slot.

                **Suggestions:**
                1. **Adjust preferred times** — Change one task's time to morning/afternoon/evening
                2. **Extend available time** — Try allocating more time for this day
                3. **Reschedule tasks** — Move lower-priority tasks to another day
                """
            )

    if scheduler.scheduled_tasks:
        st.subheader("📋 Scheduled tasks (sorted by time)")
        scheduled_data = [
            {
                "Task": t.name,
                "Time": t.preferred_time.value.capitalize() if t.preferred_time else "Anytime",
                "Duration": f"{t.duration} min",
                "Priority": "🔴" if t.priority == 3 else "🟡" if t.priority == 2 else "🟢",
            }
            for t in scheduler.scheduled_tasks
        ]
        st.table(scheduled_data)
        total_time = sum(t.duration for t in scheduler.scheduled_tasks)
        remaining_time = st.session_state.owner.available_time - total_time
        st.success(f"Total scheduled: {total_time} min | Remaining: {remaining_time} min")

    if scheduler.unscheduled_tasks:
        st.warning("**Could not fit the following tasks:**")
        unscheduled_data = [
            {"Task": t.name, "Duration": f"{t.duration} min", "Priority": t.priority}
            for t in scheduler.unscheduled_tasks
        ]
        st.table(unscheduled_data)

    with st.expander("View detailed explanations"):
        for task_id, reason in scheduler.explain_plan().items():
            st.caption(reason)
