# Creating a tuple
fruits = ("apple", "banana", "orange", "mango")

print("Tuple:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print("Length:", len(numbers))

numbers = (10, 20, 30, 40, 50, 60)

print("Original:", numbers)
print("First 3:", numbers[:3])
print("Middle:", numbers[2:5])
print("Last 3:", numbers[-3:])

student = ("Arun", 20, "Python")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

numbers = (10, 20, 10, 30, 10, 40)

# count()
print("10 occurs:", numbers.count(10), "times")

# index()
print("Position of 30:", numbers.index(30))

fruits = ("apple", "banana", "orange", "mango")


students = ("Arun", "Bala", "Kumar", "Ravi")

print("Students:")

for student in students:
    print(student)

    numbers = (10, 25, 5, 40, 15)

print("Numbers:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

#compare two tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

if tuple1 == tuple2:
    print("Both tuples are equal")
else:
    print("Tuples are different")

#length
    tuple1 = (10, 20, 30, 40)

tuple2 = tuple1

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)



fruit = input("Enter a fruit: ")

if fruit in fruits:
    print(fruit, "is present in the tuple")
else:
    print(fruit, "is not present in the tuple")

