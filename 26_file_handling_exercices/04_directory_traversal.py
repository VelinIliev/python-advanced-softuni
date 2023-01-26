from os import listdir

files = {}

for file in listdir('directory_to_traverse'):
    extension = file.split(".")[1]
    if extension not in files:
        files[extension] = []
    files[extension].append(file)

for extension, values in sorted(files.items()):
    print(f'.{extension}')
    [print(f'- - - {file}') for file in sorted(values)]