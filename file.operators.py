# File: file_operations_

# --- Step 1: Create and Write to a File ---
# 'w' mode = write (overwrite if file exists)
file = open("example.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This is the second line.\n")
file.write("File handling in Python is easy!\n")
file.close()  # Always close the file

print("✅ File created and data written successfully!\n")

# --- Step 2: Read the File ---
# 'r' mode = read
file = open("example.txt", "r")
content = file.read()  # Read entire file content
print("📖 Reading file content:")
print(content)
file.close()

# --- Step 3: Append to the File ---
# 'a' mode = append
file = open("example.txt", "a")
file.write("This line was added later using append mode.\n")
file.close()

print("\n✅ Data appended successfully!\n")

# --- Step 4: Read Line by Line ---
file = open("example.txt", "r")
print("📘 Reading line by line:")
for line in file:
    print(line.strip())  # strip() removes extra newlines
file.close()

# --- Step 5: Check if File Exists (using os module) ---
import os

if os.path.exists("example.txt"):
    print("\n✅ The file 'example.txt' exists.")
else:
    print("\n❌ The file does not exist.")

# --- Step 6: Rename the File ---
os.rename("example.txt", "new_example.txt")
print("✅ File renamed to 'new_example.txt'")

# --- Step 7: Delete the File ---
os.remove("new_example.txt")
print("🗑️ File deleted successfully!")
