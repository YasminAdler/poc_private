# import itertools

# class Soldier:
#     def __init__(self, id, job, is_sick=False, is_on_base=True):
#         self.id = id
#         self.job = job
#         self.is_sick = is_sick
#         self.is_on_base = is_on_base

#     def is_available(self):
#         return not self.is_sick and self.is_on_base

# class Mission:
#     def __init__(self, name, required_soldiers, required_job=None):
#         self.name = name
#         self.required_soldiers = required_soldiers
#         self.required_job = required_job

# def is_valid_assignment(mission, soldiers):
#     if len(soldiers) < mission.required_soldiers:
#         return False

#     if mission.required_job:
#         if not all(soldier.job == mission.required_job for soldier in soldiers):
#             return False

#     return True

# def schedule_missions(missions, soldiers, schedule={}, index=0):
#     if index == len(missions):
#         return schedule

#     mission = missions[index]
#     for combination in itertools.combinations(soldiers, mission.required_soldiers):
#         if is_valid_assignment(mission, combination):
#             schedule[mission.name] = [soldier.id for soldier in combination]
#             if schedule_missions(missions, soldiers, schedule, index + 1):
#                 return schedule
#             schedule.pop(mission.name)  # backtrack

#     return None

# # Example Usage
# soldiers = [Soldier(i, 'Infantry') for i in range(30)]  # 30 soldiers
# missions = [Mission('Station1 Guard', 2, 'Infantry'), Mission('Patrol', 8, 'Infantry')]

# schedule = schedule_missions(missions, soldiers)

# if schedule:
#     print("Schedule:", schedule)
# else:
#     print("No valid schedule found")

from constraint import Problem, AllDifferentConstraint

# Create a problem instance
problem = Problem()

# Defining variables and their possible values
soldiers = ["Alice", "Bob", "Charlie"]
tasks = ["Rest", "Guard", "Patrol"]

# Define the domain for each soldier
for soldier in soldiers:
    problem.addVariable(soldier, tasks)

# New Constraints:

# A soldier must be at rest for 8 hours - means at least 2 soldiers are at rest
for soldier in soldiers:
    problem.addConstraint(lambda a, b, c: (a == "Rest") + (b == "Rest") + (c == "Rest") >= 1, soldiers)

# Patrol is an 8-hour shift, so a soldier must have Patrol for 8 hours
# problem.addConstraint(AllDifferentConstraint(), soldiers)

# Soldiers cannot have the same task at the same time
problem.addConstraint(lambda a, b, c: len(set([a, b, c])) == 3, soldiers)

# Solve the problem
solutions = problem.getSolutions()

# Print the first solution as a schedule
if solutions:
    schedule = solutions[0]  # Select the first solution as a schedule
    for soldier, task in schedule.items():
        print(f"{soldier}: {task}")
else:
    print("No valid schedule found.")

