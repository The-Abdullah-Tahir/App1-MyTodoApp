FILENAME = 'todos.txt'


def get_todos(filename=FILENAME):
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(to_write, filename=FILENAME):
    with open(filename, 'w') as file_local:
        file_local.writelines(to_write)
