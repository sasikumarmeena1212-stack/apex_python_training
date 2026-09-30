# Python List Operations - College Student Example

students = ["Arun", "Bala", "Karthik", "Rahul"]
marks = [75, 90, 65, 85]

print("Original Student List:", students)

# 1. append()
students.append("Vijay")
print("After append():", students)

# 2. extend()
students.extend(["Ajay", "Dinesh"])
print("After extend():", students)

# 3. insert()
students.insert(1, "Kumar")
print("After insert():", students)

# 4. remove()
students.remove("Bala")
print("After remove():", students)

# 5. pop()
students.pop()
print("After pop():", students)

# 6. index()
print("Index of Karthik:", students.index("Karthik"))

# 7. count()
print("Count of Arun:", students.count("Arun"))

# 8. sort()
students.sort()
print("After sort():", students)

# 9. reverse()
students.reverse()
print("After reverse():", students)

# 10. copy()
student_copy = students.copy()
print("Copied List:", student_copy)

# 11. clear()
student_copy.clear()
print("After clear():", student_copy)

# Numeric list operations
print("\nMarks:", marks)

# 12. sum()
print("Sum of marks:", sum(marks))

# 13. min()
print("Minimum mark:", min(marks))

# 14. max()
print("Maximum mark:", max(marks))

# 15. len()
print("Number of students:", len(students))
