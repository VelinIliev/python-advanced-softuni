size = int(input())

field = []
bunny_position = []

for i in range(size):
    row = [int(x) if x.lstrip("-").isnumeric() else x for x in input().split() ]
    if "B" in row:
        bunny_position = [i, row.index("B")]
    field.append(row)

directions = ['left', 'right', 'up', 'down']
row_boundaries = range(0, len(field))
col_boundaries = range(0, len(field[0]))

max_sum = 0
max_path = []
max_direction = ""

for direction in directions:
    row = bunny_position[0]
    col = bunny_position[1]
    sum_direction = 0
    path = []
    if direction == "left":
        while True:
            col -= 1
            if col in col_boundaries and field[row][col] != "X":
                sum_direction += field[row][col]
                path.append([row, col])
            else:
                break
    elif direction == "right":
        while True:
            col += 1
            if col in col_boundaries and field[row][col] != "X":
                sum_direction += field[row][col]
                path.append([row, col])
            else:
                break
    elif direction == "up":
        while True:
            row -= 1
            if row in row_boundaries and field[row][col] != "X":
                sum_direction += field[row][col]
                path.append([row, col])
            else:
                break
    elif direction == "down":
        while True:
            row += 1
            if row in row_boundaries and field[row][col] != "X":
                sum_direction += field[row][col]
                path.append([row, col])
            else:
                break
    if sum_direction >= max_sum and len(path) >= 1:
        max_sum = sum_direction
        max_path = path
        max_direction = direction

print(max_direction)
for step in max_path:
    print(step)
print(max_sum)