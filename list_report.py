# Part C - List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Print each item with a number
number = 1

for item in items:
    print(str(number) + ". " + item)
    number += 1

# 2. Count item names with more than 4 letters
count = 0

for item in items:
    if len(item) > 4:
        count += 1

print("Items with more than 4 letters:", count)

# 3. Find the longest item using a loop comparison
longest = ""

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item:", longest)