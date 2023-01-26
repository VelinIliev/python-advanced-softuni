import os

while True:
    command = input()
    if command == "End":
        break
    action, file_name, *more = command.split("-")
    if action == 'Create':
        with open(f'{file_name}', 'w') as f:
            f.write("")
    elif action == 'Add':
        line = more[0]
        with open(f'{file_name}', 'a') as f:
            f.write(f"{line}\n")
    elif action == 'Replace':
        try:
            file = open(f'{file_name}', 'r')
        except FileNotFoundError:
            print('An error occurred')
            continue
        old_string = more[0]
        new_string = more[1]
        lines = []
        for line in file:
            if old_string in line:
                line = line.replace(old_string, new_string)
            lines.append(line)
        with open(f'{file_name}', 'w') as f:
            for line in lines:
                f.write(f"{line}")
    elif action == "Delete":
        try:
            os.remove(f'{file_name}')
        except FileNotFoundError:
            print('An error occurred')