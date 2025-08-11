# Simple To-Do List in Python

tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '3':
        if not tasks:
            print("No tasks to remove!")
        else:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
