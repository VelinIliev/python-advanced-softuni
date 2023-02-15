size = 6

matrix = [[x for x in input().split()] for row in range(size)]
position = input().split(", ")
row_, col = [int(position[0][1]), int(position[1][0])]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command, *info = input().split(", ")
    if command == 'Stop':
        break
    direction = info[0]
    row_ += directions[direction][0]
    col += directions[direction][1]
    if command == 'Create':
        value = info[1]
        if matrix[row_][col] == ".":
            matrix[row_][col] = value
    elif command == 'Update':
        value = info[1]
        if matrix[row_][col] != ".":
            matrix[row_][col] = value
    elif command == 'Delete':
        matrix[row_][col] = '.'
    elif command == 'Read':
        if matrix[row_][col] != '.':
            print(matrix[row_][col])

[print(*row, sep=" ") for row in matrix]