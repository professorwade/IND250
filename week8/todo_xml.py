import xml.etree.ElementTree as ET
from pathlib import Path
import sys
import os


def todo_app(fname):
    """start-up function for todo list app"""
    todo_list = []
    file_path = Path(fname)

    if file_path.is_file() and os.path.getsize(fname) > 0:
        try:
            tree = ET.parse(fname)
            root = tree.getroot()
            # Each task is now a dictionary: {'task': 'text', 'priority': 'level'}
            for item in root.findall('item'):
                todo_list.append({
                    'task': item.text,
                    'priority': item.get('priority', 'Low')  # Read attribute
                })
        except ET.ParseError:
            print("Warning: XML file corrupted. Starting with an empty list.")

    menu(fname, todo_list)


def update_file(fname, todo_list):
    """Sorts by priority and writes to XML file"""
    # Priority mapping for sorting
    p_map = {"High": 1, "Med": 2, "Low": 3}
    todo_list.sort(key=lambda x: p_map.get(x['priority'], 4))

    root = ET.Element("tasks")
    for item in todo_list:
        item_element = ET.SubElement(root, "item")
        item_element.text = item['task']
        # Set the priority as an XML attribute
        item_element.set('priority', item['priority'])

    tree = ET.ElementTree(root)
    tree.write(fname, encoding="utf-8", xml_declaration=True)


def menu(fname, todo_list):
    """main loop of todo list app"""
    while True:
        try:
            print("\n--- Current To-Do's (XML) ---")
            print(f"{'#':<3} {'Task':<25} {'Priority':<10}")
            print("-" * 40)

            if not todo_list:
                print("(List is empty)")
            else:
                for i, item in enumerate(todo_list, 1):
                    print(f"{i:<3} {item['task']:<25} {item['priority']:<10}")

            print("\nMenu:")
            print("1. Add Item")
            print("2. Update Item")
            print("3. Delete Item")
            print("4. Quit")

            choice = input("\nEnter choice: ").strip()

            if choice == '1':
                task = input("Enter task description: ")
                priority = input("Enter priority (High/Med/Low): ").strip().capitalize()
                todo_list.append({'task': task, 'priority': priority})
                update_file(fname, todo_list)

            elif choice == '2':  # UPDATE LOGIC
                if not todo_list:
                    print("Nothing to update!")
                    continue

                idx = int(input("Enter task number to update: ")) - 1
                if 0 <= idx < len(todo_list):
                    print(f"Updating: {todo_list[idx]['task']}")
                    new_task = input("New description (leave blank to keep current): ").strip()
                    new_pri = input("New priority (leave blank to keep current): ").strip().capitalize()

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
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'todo.xml'
    todo_app(file_path)