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
During implementation, I realized that the `Scheduler` class needed to be more flexible to accommodate additional constraints and preferences that users might have. I decided to refactor the `Scheduler` class to use a more modular approach, allowing us to easily add new scheduling algorithms or constraints in the future without having to overhaul the entire system. This change was made to improve the maintainability and scalability of our scheduler as I anticipated that users might have varying needs and preferences when it comes to scheduling their pet care tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
Our scheduler considers several constraints, including:
- Time constraints: Tasks may have specific time windows during which they can be performed (e.g., morning, afternoon, evening).
- Priority levels: Tasks can be assigned different priority levels (e.g., high, medium, low) that influence their scheduling order.
- User preferences: Users may have preferences for when certain tasks should be scheduled (e.g., preferring to walk the dog in the morning).
- How did you decide which constraints mattered most?
I decided to prioritize time constraints and user preferences over priority levels because I wanted to ensure that tasks were scheduled at times that were feasible and aligned with the user's lifestyle. For example, if a user prefers to walk their dog in the morning, I would prioritize scheduling that task during the morning time slot, even if it had a lower priority level compared to other tasks. This approach was chosen to enhance user satisfaction and ensure that the scheduling system was practical and user-centric.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff our scheduler makes is that it may not always schedule the highest priority tasks first if they conflict with user preferences or time constraints. For instance, if a high-priority task can only be performed in the evening but the user prefers to do it in the morning, the scheduler may choose to schedule it in the morning to accommodate the user's preference, even though it means that a lower-priority task might be scheduled in the evening instead. It uses a greedy approach that tries to fit tasks into preferred time slots while respecting constraints, which can lead to suboptimal scheduling in terms of priority but better alignment with user preferences.
- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable because the primary goal of the scheduler is to create a schedule that is practical and user-friendly. While it is important to consider task priorities, it is equally important to respect the user's preferences and time constraints to ensure that the schedule is actually usable and meets the user's needs. By allowing for some flexibility in scheduling based on user preferences, I can create a more personalized and satisfying experience for the user, even if it means that not all high-priority tasks are scheduled first.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI tools primarily for design brainstorming and refactoring. During the initial design phase, I used AI to generate ideas for how to structure our classes and their relationships, which helped us create a more organized and efficient UML diagram. Additionally, I used AI to assist with refactoring our code when I realized that our initial `Scheduler` class needed to be more flexible. The AI provided suggestions for how to modularize the scheduling logic, which made it easier for us to implement changes without disrupting the overall structure of our code.
- What kinds of prompts or questions were most helpful?
Prompts that asked for specific design patterns or best practices in object-oriented programming were particularly helpful. For example, asking for suggestions on how to implement a modular scheduling system or how to handle user preferences in a way that is scalable and maintainable provided us with valuable insights and guidance during the refactoring process.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
During the refactoring of the `Scheduler` class, the AI suggested a specific design pattern that involved creating multiple subclasses for different scheduling algorithms. However, I felt that this approach would add unnecessary complexity to our codebase and make it harder to maintain. Instead, I decided to implement a more flexible design that allowed us to easily switch between different scheduling algorithms without needing to create separate subclasses. This decision was based on my judgment of the tradeoff between flexibility and simplicity in our code design.
- How did you evaluate or verify what the AI suggested?
I evaluated the AI's suggestion by considering the overall maintainability and scalability of our codebase. I thought about how easy it would be to add new scheduling algorithms in the future and how the suggested design would impact our ability to make changes without introducing bugs. I also considered the complexity of the code and whether it would be easy for other developers to understand and work with. Ultimately, I decided that a more modular approach that did not require multiple subclasses would better meet our needs while still allowing for flexibility in our scheduling logic.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested several key behaviors of our scheduling logic, including:
- Task prioritization: I verified that tasks were sorted correctly based on their priority levels and durations.
- Time slot fitting: I checked that tasks were scheduled into their preferred time slots when possible, and that the scheduler respected time constraints.
- Conflict detection: I ensured that the scheduler correctly identified overlapping tasks and generated appropriate warnings for conflicts.
- Filtering: I tested that the filtering functionality for completed tasks and tasks by pet name worked as expected.

- Why were these tests important?
These tests were important because they verified that our scheduling logic was functioning correctly and that the system was able to create a practical and user-friendly schedule. By testing task prioritization, I ensured that the scheduler was respecting the importance of tasks as defined by the user. Testing time slot fitting and conflict detection was crucial to confirm that the scheduler was creating feasible schedules that respected user preferences and constraints. Finally, testing filtering functionality helped us ensure that users could easily manage and view their tasks based on their completion status and associated pets.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am fairly confident that our scheduler works correctly based on the tests I have implemented, which cover a range of key behaviors and edge cases. The tests have helped us identify and fix several issues during development, and they provide a good level of assurance that the core scheduling logic is functioning as intended. However, I recognize that there may still be edge cases that I have not covered, and there is always room for improvement in terms of test coverage and robustness.
- What edge cases would you test next if you had more time?
If I had more time, I would add tests for edge cases such as:
- Handling a large number of tasks to ensure that the scheduler can scale effectively.
- Testing tasks with unusual time preferences (e.g., tasks that can only be performed at very specific times) to verify that the scheduler can accommodate these constraints.
- Verifying that the scheduler behaves correctly when there are conflicting user preferences (e.g., two tasks that both prefer the same time slot).
- Testing the behavior of the scheduler when all tasks have the same priority level to ensure that it still creates a reasonable schedule.
- Testing the system's behavior when there are no tasks to schedule to confirm that it handles this scenario gracefully without errors.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with the overall design and implementation of our scheduling logic. I were able to create a system that effectively considers various constraints and user preferences while generating a practical schedule for pet care tasks. The modular design of our classes allows for flexibility and scalability, which is a significant achievement given the complexity of the scheduling problem I were trying to solve. Additionally, the tests I implemented provided a good level of confidence in the correctness of our scheduling logic, which is something I am proud of.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would focus on improving the user interface to make it more intuitive and user-friendly. While our current implementation allows users to create and manage tasks, I believe there is room for enhancement in terms of how the scheduled tasks are displayed and how users interact with the scheduling system. For example, I would consider adding a calendar view that visually represents the scheduled tasks, making it easier for users to see their schedule at a glance. Additionally, I would work on providing more detailed explanations for scheduling decisions, helping users understand why certain tasks were scheduled at specific times based on their preferences and constraints.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned about designing systems is the importance of flexibility and modularity in code design. By creating a modular structure for our scheduler, I were able to easily adapt and improve our scheduling logic as I encountered new requirements and constraints during development. This experience reinforced the idea that designing for change is crucial when building complex systems, as it allows for easier maintenance and scalability in the long run. Additionally, working with AI tools highlighted the importance of critical evaluation and judgment when incorporating AI suggestions into our design, ensuring that I make informed decisions that align with our project goals and user needs.
