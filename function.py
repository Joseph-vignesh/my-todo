FILEPATH = 'vic.txt'

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
"""Reads the file and stores it in the list variable called todos = [ ]"""
def write_todos( todos_arg, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
"""Writes the new_  todo items list in the text file"""

if __name__ ==  "__main__":
    print("hello")
    print(get_todos())

# NOTE: This script runs only on your local IDE
