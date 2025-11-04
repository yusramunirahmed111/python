# -----------------------------
# Python Error Handling Examples
# -----------------------------

# 1️⃣ Basic try-except
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("Error: Please enter a valid number!")

# 2️⃣ Multiple except blocks
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Error: Please enter only numbers!")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# 3️⃣ Using else (runs if no error occurs)
try:
    age = int(input("\nEnter your age: "))
except ValueError:
    print("Error: Invalid input! Please enter a number.")
else:
    print("You are", age, "years old.")

# 4️⃣ Using finally (always runs)
try:
    file = open("example.txt", "w")
    file.write("Python error handling example.")
except IOError:
    print("Error: Could not write to file.")
finally:
    file.close()
    print("File closed successfully (finally block executed).")

# 5️⃣ Handling multiple exceptions in one line
try:
    a = int(input("\nEnter number a: "))
    b = int(input("Enter number b: "))
    print("Division result:", a / b)
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)

# 6️⃣ Custom Exception Example
try:
    age = int(input("\nEnter your age again: "))
    if age < 18:
        raise Exception("You must be at least 18 years old.")
    print("Access granted.")
except Exception as e:
    print("Custom Error:", e)

# -----------------------------
# End of Examples
# -----------------------------
