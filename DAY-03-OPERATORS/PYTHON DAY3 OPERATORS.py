# ==========================================
# PYTHON OPERATORS - ALL TYPES
# ==========================================

# 1. ARITHMETIC OPERATORS
print("===== 1. ARITHMETIC OPERATORS =====")

a = 10
b = 3

print("Addition       :", a + b)   # +
print("Subtraction    :", a - b)   # -
print("Multiplication :", a * b)   # *
print("Division       :", a / b)   # /
print("Floor Division :", a // b)  # //
print("Modulus        :", a % b)   # %
print("Exponent       :", a ** b)  # **


# 2. ASSIGNMENT OPERATORS
print("\n===== 2. ASSIGNMENT OPERATORS =====")

x = 10
print("x =", x)

x += 5
print("x += 5  :", x)

x -= 3
print("x -= 3  :", x)

x *= 2
print("x *= 2  :", x)

x /= 4
print("x /= 4  :", x)

x //= 2
print("x //= 2 :", x)

x %= 3
print("x %= 3  :", x)

x **= 2
print("x **= 2 :", x)


# 3. COMPARISON OPERATORS
print("\n===== 3. COMPARISON OPERATORS =====")

p = 10
q = 20

print("p == q :", p == q)   # Equal
print("p != q :", p != q)   # Not equal
print("p > q  :", p > q)    # Greater than
print("p < q  :", p < q)    # Less than
print("p >= q :", p >= q)   # Greater than or equal
print("p <= q :", p <= q)   # Less than or equal


# 4. LOGICAL OPERATORS
print("\n===== 4. LOGICAL OPERATORS =====")

age = 20
has_id = True

print("AND :", age >= 18 and has_id)
print("OR  :", age >= 18 or has_id)
print("NOT :", not has_id)


# 5. IDENTITY OPERATORS
print("\n===== 5. IDENTITY OPERATORS =====")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 is not list3 :", list1 is not list3)


# 6. MEMBERSHIP OPERATORS
print("\n===== 6. MEMBERSHIP OPERATORS =====")

numbers = [10, 20, 30, 40, 50]

print("20 in numbers     :", 20 in numbers)
print("60 in numbers     :", 60 in numbers)
print("60 not in numbers :", 60 not in numbers)
