import json
from pathlib import Path
import sys


def todo_app(fname):
    """start-up function for todo list app"""
    file_path = Path(fname)
    if file_path.is_file() and file_path.stat().st_size > 0:
        with open(fname, 'r', encoding="utf-8") as f:
            try:
                todo_list = json.load(f)
            except json.JSONDecodeError:
                todo_list = []
    else:
        todo_list = []
    menu(fname, todo_list)


def update_file(fname, todo_list):
    """Sorts by priority and writes to JSON file"""
    p_map = {"High": 1, "Med": 2, "Low": 3}
    todo_list.sort(key=lambda x: p_map.get(x.get('priority', 'Low'), 4))
    with open(fname, 'w', encoding="utf-8") as f:
        json.dump(todo_list, f, indent=4)


def menu(fname, todo_list):
    """main loop of todo list app"""
    while True:
        try:
            print("\n--- Current To-Do's ---")
            print(f"{'#':<3} {'Task':<25} {'Priority':<10}")
            print("-" * 40)

            if not todo_list:
                print("(List is empty)")
            else:
                for i, item in enumerate(todo_list, 1):
                    print(f"{i:<3} {item['task']:<25} {item['priority']:<10}")

            print("\nMenu:")
            print("1. Add Item")
            print("2. Update Item")  # New Option
            print("3. Delete Item")
            print("4. Quit")

            choice = input("\nEnter choice: ").strip()

            if choice == '1':
                task = input("Enter task description: ")
                priority = input("Enter priority (High/Med/Low): ").strip().capitalize()
                todo_list.append({"task": task, "priority": priority})
                update_file(fname, todo_list)

            elif choice == '2':  # UPDATE LOGIC
                if not todo_list:
                    print("Nothing to update!")
                    continue

                idx = int(input("Enter task number to update: ")) - 1
                if 0 <= idx < len(todo_list):
                    print(f"Updating: {todo_list[idx]['task']}")
                    new_task = input("Enter new description (leave blank to keep current): ")
                    new_pri = input("Enter new priority (leave blank to keep current): ").strip().capitalize()

                    if new_task:
                        todo_list[idx]['task'] = new_task
                    if new_pri in ["High", "Med", "Low"]:
                        todo_list[idx]['priority'] = new_pri

                    update_file(fname, todo_list)
                    print("Task updated!")
                else:
                    print("Invalid task number.")

            elif choice == '3':
                if todo_list:
                    idx = int(input("Enter number to delete: ")) - 1
                    if 0 <= idx < len(todo_list):
                        todo_list.pop(idx)
                        update_file(fname, todo_list)
                    else:
                        print("Invalid task number.")
                else:
                    print("Nothing to delete!")

            elif choice == '4':
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'todo.json'
    todo_app(file_path)