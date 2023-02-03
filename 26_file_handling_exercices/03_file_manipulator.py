import os


def create_file(file_name):
    with open(f'{file_name}', 'w') as f:
        f.write("")


def add_to_file(file_name, info):
    line = info[0]
    with open(f'{file_name}', 'a') as f:
        f.write(f"{line}\n")


def replace_in_file(file_name, info):
    try:
        old_string = info[0]
        new_string = info[1]
        with open(f'{file_name}', 'r') as f:
            file = f.read()
        file = file.replace(old_string, new_string)
        with open(f'{file_name}', 'w') as f:
            for line in file:
                f.write(f"{line}")
    except FileNotFoundError:
        print('An error occurred')


def delete_file(file_name):
    try:
        os.remove(f'{file_name}')
    except FileNotFoundError:
        print('An error occurred')


command = input()

while command != "End":
    action, file_name, *info = command.split("-")
    if action == 'Create':
        create_file(file_name)
    elif action == 'Add':
        add_to_file(file_name, info)
    elif action == 'Replace':
        replace_in_file(file_name, info)
    elif action == "Delete":
        delete_file(file_name)
    command = input()
