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

    # Create a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 1. append() → Add item at the end
fruits.append("mango")
print("After append:", fruits)

# 2. insert() → Add item at a specific index
fruits.insert(1, "orange")  # at index 1
print("After insert:", fruits)

# 3. remove() → Remove an item by value
fruits.remove("banana")
print("After remove:", fruits)

# 4. pop() → Remove item by index (default last)
fruits.pop(2)
print("After pop:", fruits)

# 5. clear() → Remove all items
copy_list = fruits.copy()
copy_list.clear()
print("After clear:", copy_list)

# 6. index() → Find index of a value
print("Index of apple:", fruits.index("apple"))

# 7. count() → Count occurrences
numbers = [1, 2, 2, 3, 4, 2, 5]
print("Count of 2:", numbers.count(2))

# 8. sort() → Sort list (ascending by default)
numbers.sort()
print("Sorted numbers:", numbers)

# 9. reverse() → Reverse order
numbers.reverse()
print("Reversed numbers:", numbers)

# 10. copy() → Make a shallow copy
new_fruits = fruits.copy()
print("Copied list:", new_fruits)

# 11. extend() → Add elements of another list
fruits.extend(["grape", "melon"])
print("After extend:", fruits)





