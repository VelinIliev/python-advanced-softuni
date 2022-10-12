matrix = []

for row in range(6):
    new_row = [x for x in input().split(" ")]
    matrix.append(new_row)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}
first_position = input().split(", ")
row = int(first_position[0].lstrip("("))
col = int(first_position[1].rstrip(")"))
boundaries = range(0, 6)
current_position = [row, col]

while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = command.split(", ")
        action = command[0]
        direction = command[1]
        new_row = current_position[0] + directions[direction][0]
        new_col = current_position[1] + directions[direction][1]

    if new_row in boundaries and new_col in boundaries:
        if action == "Create":
            value = command[2]
            if matrix[new_row][new_col] == ".":
                matrix[new_row][new_col] = value
        elif action == "Update":
            value = command[2]
            if matrix[new_row][new_col].isalnum():
                matrix[new_row][new_col] = value
        elif action == "Delete":
            if matrix[new_row][new_col].isalnum():
                matrix[new_row][new_col] = "."
        elif action == "Read":
            if matrix[new_row][new_col].isalnum():
                print(matrix[new_row][new_col])
        current_position = [new_row, new_col]

for row in matrix:
    print(" ".join(row))