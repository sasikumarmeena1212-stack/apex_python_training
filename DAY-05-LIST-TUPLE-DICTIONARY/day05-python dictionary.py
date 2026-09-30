#creaqting a dictionary
student = {
    "name": "Aushvanth",
    "age": 20,
    "department": "Civil Engineering"
}

print(student)

#accessing values
print(student["name"])
print(student["department"])

#adding new item
student["college"] = "Sudharsan Engineering College"

print(student)

#updating a value
student["age"] = 21

#removing a item
student.pop("age")

#using delete
del student["college"]

#important dictionary methods
student = {
    "name": "Aushvanth",
    "age": 20,
    "department": "Civil"
}

print(student.keys())
print(student.values())
print(student.items())

#using get()
print(student.get("name"))
print(student.get("marks"))

#key and values
for key, value in student.items():
    print(key, ":", value)

    

    #nested dictionary
    students = {
    "student1": {
        "name": "Aushvanth",
        "mark": 85
    },
    "student2": {
        "name": "Rahul",
        "mark": 90
    }
}

print(students["student1"]["name"])
