import json


def load_data():
    try:
        with open("tasks.txt", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def save_data_helper(tasks):
    with open("tasks.txt", "w") as file:
        json.dump(tasks, file)


def view_all_task(tasks):
    print("\n")
    print("*" * 80)
    for index, task in enumerate(tasks, start=1):
        status = "✅ Done" if task.get("done") else "❌ Not Done"
        print(
            f"{index}. Task) {task.get('task')}. Category) {task.get('category')}. Priority) {task.get('priority')}. Status) {status}"
        )
    print("\n")
    print("*" * 70)


def add_new_task(tasks):
    task = input("Enter task name: ").capitalize().strip()
    category = input("Enter task category: ").capitalize().strip()
    priority = input("Enter task priority(Low/Medium/High): ").capitalize().strip()
    mark_done = False
    tasks.append(
        {"task": task, "category": category, "priority": priority, "done": mark_done}
    )
    save_data_helper(tasks)


def mark_task_done(tasks):
    view_all_task(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ").strip())
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            save_data_helper(tasks)
            print(f"** Task [{index}] marked as completed. ")
        else:
            print("Invalid index task selected. ")
    except ValueError:
        print("Please enter a valid task number. ")


def delete_all_task(tasks):
    view_all_task(tasks)
    index = int(input("Enter task number to deleted: ").strip())
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print(f"Task {index} deleted successfully. ")
        save_data_helper(tasks)
    else:
        print("Invalid task number selected. ")


def update_task(tasks):
    view_all_task(tasks)
    index = int(input("Enter task number to update: ").strip())
    if 1 <= index <= len(tasks):
        task = input("Enter task name: ").capitalize().strip()
        category = input("Enter task category: ").capitalize().strip()
        priority = input("Enter task priority(Low/Medium/High): ").capitalize().strip()
        mark_done = True
        tasks[index - 1] = {
            "task": task,
            "category": category,
            "priority": priority,
            "done": mark_done,
        }
    else:
        print("Invalid task selected. ")
        save_data_helper(tasks)


def search_category(tasks):
    print("\nSearch By: ")
    print("1. Category")
    print("2. Priority")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        keyword = input("Enter category to search: ").capitalize().strip()
        results = [task for task in tasks if task.get("category") == keyword]

    elif choice == "2":
        keyword = (
            input("Enter priority to search (Low/Medium/High): ").capitalize().strip()
        )
        results = [task for task in tasks if task.get("priority") == keyword]

    else:
        print("Invalid choice.")
        return

    if results:
        print(f"Tasks matching: {keyword}")
        view_all_task(results)
    else:
        print(f"No tasks found for '{keyword}'.")


def main():
    tasks = load_data()
    while True:
        print("\n  Daily Task Tracker | choose option")
        print("1. View All Tasks")
        print("2. Add a New Task")
        print("3. Mark a Task as Done")
        print("4. Delete a Task")
        print("5. Search by Category or Priority")
        print("6. Update a Task")
        print("7. Exit App")
        choose_option = input("\nEnter an option: ").strip()
        if choose_option == "1":
            view_all_task(tasks)
        elif choose_option == "2":
            add_new_task(tasks)
        elif choose_option == "3":
            mark_task_done(tasks)
        elif choose_option == "4":
            delete_all_task(tasks)
        elif choose_option == "5":
            search_category(tasks)
        elif choose_option == "6":
            update_task(tasks)
        elif choose_option == "7":
            print("Exiting.. Good Bye!")
            break
        else:
            print("Invalid input.Enter option between 1 to 6. ")


if __name__ == "__main__":
    main()
