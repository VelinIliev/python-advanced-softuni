import os

files = {}

home_directory = input()
directories_to_traverse = [home_directory]


def extract_files(current_directory):
    for file in os.listdir(current_directory):
        if os.path.isfile(f'{current_directory}/{file}'):
            *name, extension = file.split(".")
            if not name:
                continue
            if extension not in files:
                files[extension] = []
            files[extension].append(file)
        else:
            directories_to_traverse.append(f'{current_directory}/{file}')


def write_summary_to_file():
    with open('report.txt', 'w') as f:
        for extension, values in sorted(files.items()):
            f.write(f'.{extension} - {len(values)}\n')
            [f.write(f'- - - {file}\n') for file in sorted(values)]
            print(f'.{extension} - {len(values)}')
            [print(f'- - - {file}') for file in sorted(values)]


while directories_to_traverse:
    current_directory = directories_to_traverse.pop(0)
    try:
        extract_files(current_directory)
    except FileNotFoundError:
        print("Directory Not Found")

write_summary_to_file()
