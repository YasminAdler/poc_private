
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

