student = {"name": "Arun", "marks": 88}
student["age"] = 20  
print(student)

""
student = {"name": "Arun", "marks": 88}
student["marks"] = 95  
print(student)

""

keys = ["name", "age", "city"]
values = ["Arun", 20, "Chennai"]
student = dict(zip(keys, values))
print(student)

""
students = {
    "Arun": 88,
    "Bala": 92,
    "Charan": 85,
    "Divya": 95,
    "Esha": 90
}
highest = max(students, key=students.get)
print("Student with highest marks:", highest)
print("Marks:", students[highest])

""
cubes = {}
for i in range(1, 6):
    cubes[i] = i**3
print(cubes)
