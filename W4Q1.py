students = {
    "Henry": 40,
    "Sara": 91,
    "John": 70,
    "Zoya": 88
}

print("Students scoring above 75:")

for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)
