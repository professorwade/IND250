"""module which provides a means for testing the existence of a file"""
from pathlib import Path

def todo_app():
    """start-up function for todo list app"""
    todo_list = [] #create empty list
    # TODO: See if file is present and if so, read into todo_list
    menu(todo_list)

def update_file(todo_list):
    """Function to write active list to backup file todo.txt"""

def menu(todo_list):
    """main loop of todo list app"""
    while True:
        try: #catch any errors and don't let the app crash
            print("\nTo-Do's")

            # TODO: Implement reading list

            print("\nTo Do List") # print menu
            print("1. Add Item")
            print("2. Delete Item")
            print("3. Quit\n")
            command = input("Enter Command: ")

            if command[0] == '1': # look at first character of input
                pass # TODO: Implement Add Item
            elif command[0] == '2':
                pass # TODO: Implement Delete Item
            elif command[0] == '3':
                pass # TODO: Implement quit
        except ValueError as e:
            print("Error caught:", e)

if __name__ == '__main__':
    todo_app() # launch app
