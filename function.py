# -----------------------------
# All Function Examples 
# -----------------------------

# 1️⃣ Simple Function (no parameters)
def greet():
    print("Hello! Welcome to Python Functions.")

# 2️⃣ Function with Parameters
def greet_user(name):
    print("Hello,", name)

# 3️⃣ Function with Return Value
def add(a, b):
    return a + b

# 4️⃣ Function with Default Parameter
def welcome(name="Guest"):
    print("Welcome,", name)

# 5️⃣ Function Returning Multiple Values
def calculate(a, b):
    add = a + b
    sub = a - b
    return add, sub

# 6️⃣ Function with Loop
def print_numbers(limit):
    print("Numbers from 1 to", limit)
    for i in range(1, limit + 1):
        print(i, end=" ")
    print()  # new line

# 7️⃣ Lambda Function (One-line anonymous function)
square = lambda x: x * x


# -----------------------------
# Function Calls / Outputs
# -----------------------------

# Simple function
greet()

# Function with parameter
greet_user("Alice")
greet_user("John")

# Function with return value
result = add(10, 5)
print("Addition Result:", result)

# Function with default parameter
welcome("Ali")
welcome()

# Function returning multiple values
sum_result, sub_result = calculate(15, 8)
print("Sum:", sum_result)
print("Subtraction:", sub_result)

# Function with loop
print_numbers(5)

# Lambda function
print("Square of 6 is:", square(6))

# -----------------------------
# End of Program
# -----------------------------
