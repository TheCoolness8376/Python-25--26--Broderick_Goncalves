# Challenge 5 Starter Code

# 1) Add 5 student names to the list (with one duplicate to demonstrate removal)
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"]

# 2) Convert the list to a set to remove duplicates
unique_students = set(students)

# 3) Store student names and grades in a dictionary
# Ensure grades exist for each unique student
grades = {
    "Alice": 85,
    "Bob": 67,
    "Charlie": 92,
    "David": 73,
    "Eve": 88
}

# 4) Print all students with grades above 70
print("Students with grades above 70:")
for student in sorted(unique_students):
    grade = grades.get(student)
    if grade is not None and grade > 70:
        print(f"{student}: {grade}")

# --------------- Q & A --------------- #
# 1) A list can make things stored still be changed, while in a tuple the things stored can not be changed
# 2) Sets are unordered because there are no duplicates
# 3) Dictionaries should be used when there are multiple values needed for a single variable