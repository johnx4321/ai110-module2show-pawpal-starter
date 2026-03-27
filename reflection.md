# PawPal+ Project Reflection

## 1. System Design

- Task Management System - User should be able to create, view, and manage tasks related to pet care (feeding, walking, vet appointments).
- Constraint-aware and weighted scheduling - The system should consider constraints such as time, priority, and user preferences when scheduling tasks.
- Display to user and explain choice - The system should display the scheduled tasks to the user and provide explanations for why certain tasks were scheduled at specific times.

**a. Initial design**

- Briefly describe your initial UML design.
Our initial UML design included the following classes:
- `Task`: Represents a pet care task, with attributes such as name, description, priority, and time constraints.
- `Scheduler`: Responsible for scheduling tasks based on their constraints and priorities.
- `UserInterface`: Handles interactions with the user, allowing them to create and manage tasks, and view the scheduled tasks along with explanations.  
It was designed to separate concerns, with `Task` handling the data representation of tasks, `Scheduler` managing the logic for scheduling, and `UserInterface` focusing on user interactions and display.
- What classes did you include, and what responsibilities did you assign to each?
The `Task` class was responsible for encapsulating the details of each pet care task, including its name, description, priority level, and any time constraints. The `Scheduler` class was tasked with implementing the logic to schedule tasks based on their attributes, ensuring that constraints were respected and priorities were considered. The `UserInterface` class was designed to facilitate user interactions, allowing users to create new tasks, view existing tasks, and see the scheduled tasks along with explanations for the scheduling decisions.

**b. Design changes**

- Did your design change during implementation?
Yes
- If yes, describe at least one change and why you made it.
During implementation, we realized that the `Scheduler` class needed to be more flexible to accommodate additional constraints and preferences that users might have. We decided to refactor the `Scheduler` class to use a more modular approach, allowing us to easily add new scheduling algorithms or constraints in the future without having to overhaul the entire system. This change was made to improve the maintainability and scalability of our scheduler as we anticipated that users might have varying needs and preferences when it comes to scheduling their pet care tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
Our scheduler considers several constraints, including:
- Time constraints: Tasks may have specific time windows during which they can be performed (e.g., morning, afternoon, evening).
- Priority levels: Tasks can be assigned different priority levels (e.g., high, medium, low) that influence their scheduling order.
- User preferences: Users may have preferences for when certain tasks should be scheduled (e.g., preferring to walk the dog in the morning).
- How did you decide which constraints mattered most?
We decided to prioritize time constraints and user preferences over priority levels because we wanted to ensure that tasks were scheduled at times that were feasible and aligned with the user's lifestyle. For example, if a user prefers to walk their dog in the morning, we would prioritize scheduling that task during the morning time slot, even if it had a lower priority level compared to other tasks. This approach was chosen to enhance user satisfaction and ensure that the scheduling system was practical and user-centric.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff our scheduler makes is that it may not always schedule the highest priority tasks first if they conflict with user preferences or time constraints. For instance, if a high-priority task can only be performed in the evening but the user prefers to do it in the morning, the scheduler may choose to schedule it in the morning to accommodate the user's preference, even though it means that a lower-priority task might be scheduled in the evening instead. It uses a greedy approach that tries to fit tasks into preferred time slots while respecting constraints, which can lead to suboptimal scheduling in terms of priority but better alignment with user preferences.
- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable because the primary goal of the scheduler is to create a schedule that is practical and user-friendly. While it is important to consider task priorities, it is equally important to respect the user's preferences and time constraints to ensure that the schedule is actually usable and meets the user's needs. By allowing for some flexibility in scheduling based on user preferences, we can create a more personalized and satisfying experience for the user, even if it means that not all high-priority tasks are scheduled first.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
