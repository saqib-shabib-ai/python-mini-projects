# What are list Comprehensions
# Basic  Syntax And Example 
'''[expression for item in iterable if condition]'''

squares = [x**2 for x in range(10)]
print(squares)

# Another example
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

# Filtring with list Comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# Another example
names = ["saqib", "ali", "muazam", "gohar", "osama", "abdullah", "muzi"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Using Conditional Statements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lables = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(lables)

# Day 14: Student Grade Manager
# Step 1: Get Student Score

student_score = input("Enter student score separated by commas: ")
scores = [int(score) for score in student_score.split(",")]

# Step 2: Assign Grade using list comprehendion
grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in scores
]

# Step 3: Filter Passing and Failing student
passing_students = [score for score in scores if score >= 60]
failing_students = [score for score in scores if score < 60]

# Step 4: Display the Results
print("\n---- Student Grades ----")
for i, (score , grade) in enumerate(zip(scores , grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")

print("\n----- Passing and Failing Students -----")
print("Passing Student:", passing_students)
print("Failing Student:", failing_students)
