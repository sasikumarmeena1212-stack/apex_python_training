
import math

while True:
    print("\n===== AREA CALCULATOR =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        radius = float(input("Enter radius: "))
        area = math.pi * radius * radius
        print("Area of Circle =", int(area))

    elif choice == 2:
        side = float(input("Enter side: "))
        area = side * side
        print("Area of Square =", int(area))

    elif choice == 3:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        area = length * breadth
        print("Area of Rectangle =", int(area))

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

    for i in range(1):
        print("Calculation completed.")
