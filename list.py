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
