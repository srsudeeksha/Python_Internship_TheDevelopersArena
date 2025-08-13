# to_do_list.py
FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"❌ Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")

def add_task(tasks):
    task = input("📝 Enter a new task: ")
    if task.strip():
        tasks.append(task.strip())
        save_tasks(tasks)
        print("✅ Task added!")
    else:
        print("⚠️ Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("📂 No tasks found.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("❌ Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed_task}' deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
