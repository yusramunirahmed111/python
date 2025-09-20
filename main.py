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
# End of Examples
# -------------------------
