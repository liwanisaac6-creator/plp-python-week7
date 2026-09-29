# Part B - Shopping List Manager

shopping_list = []

while True:
    choice = input("Choose: add / remove / show / done: ").lower()

    if choice == "add":
        item = input("Enter item: ")
        shopping_list.append(item)
        print(item, "was added.")

    elif choice == "remove":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "was removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("Shopping List:")
        for item in shopping_list:
            print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")