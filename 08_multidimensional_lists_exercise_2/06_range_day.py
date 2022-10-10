matrix = []
start_position = []
targets = []
hit_targets = []

for row in range(5):
    new_row = input().split()
    if "A" in new_row:
        start_position = [row, new_row.index("A")]
    if "x" in new_row:
        for col in range(5):
            if new_row[col] == "x":
                targets.append([row, col])
    matrix.append(new_row)

number_of_commands = int(input())
boundaries = range(0, 5)
row = start_position[0]
col = start_position[1]

for n in range(number_of_commands):
    command = [int(x) if x.isnumeric() else x for x in input().split()]
    action = command[0]
    direction = command[1]
    if action == "move":
        steps = command[2]
        matrix[row][col] = "."
        if direction == "left" and col - steps in boundaries and matrix[row][col - steps] == ".":
            col -= steps
        elif direction == "right" and col + steps in boundaries and matrix[row][col + steps] == ".":
            col += steps
        elif direction == "up" and row - steps in boundaries and matrix[row - steps][col] == ".":
            row -= steps
        elif direction == "down" and row + steps in boundaries and matrix[row + steps][col] == ".":
            row += steps
        matrix[row][col] = "A"
    elif action == "shoot":
        if direction == "down" or direction == "up":
            if direction == "down":
                start, end, step = row, 5, 1
            else:
                start, end, step = row, -1, -1
            for row1 in range(start, end, step):
                if matrix[row1][col] == "x":
                    targets.remove([row1, col])
                    matrix[row1][col] = "."
                    hit_targets.append([row1, col])
                    break
        elif direction == "left" or direction == "right":
            if direction == "left":
                start, end, step = col, -1, -1
            else:
                start, end, step = col, 5, 1
            for col1 in range(start, end, step):
                if matrix[row][col1] == "x":
                    targets.remove([row, col1])
                    matrix[row][col1] = "."
                    hit_targets.append([row, col1])
                    break
    if len(targets) == 0:
        break
    print()

if targets:
    print(f'Training not completed! {len(targets)} targets left.')
else:
    print(f'Training completed! All {len(hit_targets)} targets hit.')
for target in hit_targets:
    print(target)