"""module which provides a means for testing the existence of a file"""
from pathlib import Path
import sys # gives access to command line arguments

def todo_app(fname):
    """start-up function for todo list app"""
    todo_list = [] #create empty list
    file_path = Path(fname) # name of task file
    if file_path.is_file(): # if present, read todo's
        with open(fname, 'r', encoding="utf-8") as todos:
            for todo in todos:
                todo_list.append(todo.strip())
    menu(fname, todo_list)

def update_file(fname, todo_list):
    """Function to write active list to backup file todo.txt"""
    with open(fname, 'w', encoding="utf-8") as todos_file:
        for todo in todo_list: # iterate through list collection
            print(todo,file=todos_file)  # or todos_file.write(todo + '\n')

def menu(fname, todo_list):
    """main loop of todo list app"""
    while True:
        try: #catch any errors and don't let the app crash
            print("\nTo-Do's")
            count = 1
            for todo in todo_list:
                print(f'{count}. {todo}') # print tasks in list
                count += 1 # count used to match to task number in list (off by 1)

            print("\nTo Do List") # print menu
            print("1. Add Item")
            print("2. Delete Item")
            print("3. Quit\n")
            command = input("Enter Command: ")

            if command[0] == '1': # look at first character of input
                item = input("Enter task description: ")
                todo_list.append(item)
                update_file(fname, todo_list)
            elif command[0] == '2':
                if len(todo_list) != 0:
                    item = input("Enter number of task to delete: ")
                    item_num = int(item[0]) # need a number here
                    for val in range(len(todo_list)):
                        if item_num - 1 == val:
                            todo_list.pop(val) # remove specified task
                            update_file(fname, todo_list)
                else:
                    print("Your todo list is empty!") # duh!
            elif command[0] == '3':
                break # break out of while and terminate program
        except ValueError as e:
            print("Error caught:", e)

if __name__ == '__main__':
    if len(sys.argv) > 1: # the filename is always passed, more than one and there are arguments passed
        file_path = sys.argv[1] # assume the argument passed is the todo list filename
    else:
        file_path = 'todo.txt'
    todo_app(file_path) # launch app
