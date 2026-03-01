import csv
from pathlib import Path
import sys


def todo_app(fname):
    """start-up function for todo list app"""
    todo_list = []
    file_path = Path(fname)

    if file_path.is_file() and file_path.stat().st_size > 0:
        with open(fname, 'r', encoding="utf-8", newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip the header row
            for row in reader:
                if row:
                    todo_list.append(row)

    menu(fname, todo_list)


def update_file(fname, todo_list):
    """Sorts by priority and writes list to file as a CSV"""
    # Priority mapping for sorting
    p_map = {"High": 1, "Med": 2, "Low": 3}
    todo_list.sort(key=lambda x: p_map.get(x[1], 4))

    with open(fname, 'w', encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Priority"])
        writer.writerows(todo_list)


def menu(fname, todo_list):
    """main loop of todo list app"""
    while True:
        try:
            print("\n--- Current To-Do List (CSV) ---")
            print(f"{'#':<3} {'Task':<25} {'Priority':<10}")
            print("-" * 40)

            if not todo_list:
                print("(List is empty)")
            else:
                for i, (task, priority) in enumerate(todo_list, 1):
                    print(f"{i:<3} {task:<25} {priority:<10}")

            print("\nMenu:")
            print("1. Add Item")
            print("2. Update Item")
            print("3. Delete Item")
            print("4. Quit")

            choice = input("\nEnter choice: ").strip()

            if choice == '1':
                task = input("Enter task description: ")
                priority = input("Enter priority (High/Med/Low): ").strip().capitalize()
                todo_list.append([task, priority])
                update_file(fname, todo_list)

            elif choice == '2':  # UPDATE LOGIC
                if not todo_list:
                    print("List is empty. Nothing to update.")
                    continue

                idx = int(input("Enter task number to update: ")) - 1
                if 0 <= idx < len(todo_list):
                    current_task, current_pri = todo_list[idx]
                    print(f"Updating: {current_task} ({current_pri})")

                    new_task = input(f"New description (leave blank to keep '{current_task}'): ").strip()
                    new_pri = input(f"New priority (leave blank to keep '{current_pri}'): ").strip().capitalize()

                    if new_task:
                        todo_list[idx][0] = new_task
                    if new_pri in ["High", "Med", "Low"]:
                        todo_list[idx][1] = new_pri

                    update_file(fname, todo_list)
                    print("Task updated and list re-sorted!")
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
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'todo.csv'
    todo_app(file_path)