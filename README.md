# Python Week 7 - Shopping List Manager

This assignment practices Python lists, indexes, append, remove, membership checks, loops, and list reporting.

## Files

- `list_warmup.py` - Demonstrates list creation, index access, append, remove, and len().
- `shopping_list.py` - Provides an interactive shopping list manager using add, remove, show, and done commands.
- `list_report.py` - Prints a numbered shopping list, counts item names with more than 4 letters, and finds the longest item.
- `screenshots/` - Contains screenshots showing each program running.

## Why is it safer to check `in` before calling `.remove()`?

Checking `in` first is safer because `.remove()` causes a `ValueError` if the item is not in the list. Using `in` allows the program to check whether the item exists before trying to remove it, preventing the program from crashing.