print("hello world")
print ("first name : hello")
print ("last name : world")
# -------------------------
# Python Data Types Examples
# -------------------------

# 1. Numeric Types
print("=== Numeric Types ===")
x = 10                  # int
y = 3.14                # float
z = 2 + 3j              # complex
print(x, type(x))
print(y, type(y))
print(z, type(z))

# 2. Sequence Types
print("\n=== Sequence Types ===")
name = "Python"         # str
fruits = ["apple", "banana", "mango"]  # list
numbers = (1, 2, 3, 4)  # tuple
print(name, type(name))
print(fruits, type(fruits))
print(numbers, type(numbers))

# 3. Mapping Type
print("\n=== Mapping Type ===")
student = {"name": "Ali", "age": 20, "grade": "A"}  # dict
print(student, type(student))

# 4. Set Types
print("\n=== Set Types ===")
unique_numbers = {1, 2, 3, 3, 4}  # set
fs = frozenset([1, 2, 3])         # frozenset
print(unique_numbers, type(unique_numbers))
print(fs, type(fs))

# 5. Boolean Type
print("\n=== Boolean Type ===")
is_active = True
print(is_active, type(is_active))

# 6. Binary Types
print("\n=== Binary Types ===")
b = b"Hello"                      # bytes
ba = bytearray([65, 66, 67])       # bytearray
mv = memoryview(b"Python")         # memoryview
print(b, type(b))
print(ba, type(ba))
print(mv, type(mv))

# -------------------------
# Python Operators Examples
# -------------------------

a = 10
b = 3

print("=== 1. Arithmetic Operators ===")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponent (power)
print("a // b =", a // b) # Floor Division

print("\n=== 2. Assignment Operators ===")
x = 5
print("x =", x)
x += 2   # x = x + 2
print("x += 2 ->", x)
x -= 1   # x = x - 1
print("x -= 1 ->", x)
x *= 3   # x = x * 3
print("x *= 3 ->", x)
x /= 2   # x = x / 2
print("x /= 2 ->", x)
x %= 4   # x = x % 4
print("x %= 4 ->", x)
x **= 2  # x = x ** 2
print("x **= 2 ->", x)
x //= 2  # x = x // 2
print("x //= 2 ->", x)

print("\n=== 3. Comparison Operators ===")
print("a == b ->", a == b)
print("a != b ->", a != b)
print("a > b  ->", a > b)
print("a < b  ->", a < b)
print("a >= b ->", a >= b)
print("a <= b ->", a <= b)

print("\n=== 4. Logical Operators ===")
x = True
y = False
print("x and y ->", x and y)
print("x or y  ->", x or y)
print("not x   ->", not x)

print("\n=== 5. Bitwise Operators ===")
m = 6   # (binary 110)
n = 3   # (binary 011)
print("m & n =", m & n)   # AND
print("m | n =", m | n)   # OR
print("m ^ n =", m ^ n)   # XOR
print("~m    =", ~m)      # NOT (invert bits)
print("m << 1 =", m << 1) # Left shift
print("m >> 1 =", m >> 1) # Right shift

print("\n=== 6. Membership Operators ===")
my_list = [1, 2, 3, 4, 5]
print("3 in my_list ->", 3 in my_list)
print("10 not in my_list ->", 10 not in my_list)

print("\n=== 7. Identity Operators ===")
p = [1, 2, 3]
q = [1, 2, 3]
r = p
print("p is q ->", p is q)       # False (different objects)
print("p is r ->", p is r)       # True  (same object)
print("p is not q ->", p is not q)

# Function to calculate square of a number
def square(num):
    return num * num
# comparision operators examples
a = 10
b = 5

print("a == b :", a == b)   # Equal to
print("a != b :", a != b)   # Not equal to
print("a > b  :", a > b)    # Greater than
print("a < b  :", a < b)    # Less than
print("a >= b :", a >= b)   # Greater than or equal to
print("a <= b :", a <= b)   # Less than or equal to


# if - else -elif conditions 
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Calling the function
print("Square of 5 is:", square(5))
print("Square of 9 is:", square(9))

# Dictionary of a student
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Accessing dictionary values
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])

# Adding a new key-value
student["course"] = "Computer Science"
print("Updated Dictionary:", student)

# For loop example
print("For loop example:")
for i in range(1, 6):   # 1 to 5
    print("Number:", i)

# While loop example
print("\nWhile loop example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1



