import os
from os import listdir, getcwd

files = {}

for file in listdir('directory_to_traverse'):
    extension = file.split(".")[1]
    if extension not in files:
        files[extension] = []
    files[extension].append(file)

for extension, values in sorted(files.items()):
    print(f'.{extension}')
    [print(f'- - - {file}') for file in sorted(values)]

with open('report.txt', 'w') as f:
    for extension, values in sorted(files.items()):
        f.write(f'.{extension}\n')
        [f.write(f'- - - {file}\n') for file in sorted(values)]

print('******')
print(listdir())
# os.mkdir("test")