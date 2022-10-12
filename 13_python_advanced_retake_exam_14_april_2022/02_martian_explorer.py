field = []
starting_position = []
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}
deposits = {
    "W": 0,
    "M": 0,
    "C": 0,
    "R": 0,
}
for row in range(6):
    new_row = input().split()
    field.append(new_row)
    if "E" in new_row:
        starting_position = [row, new_row.index("E")]
    # for deposit in deposits:
    #     if deposit in new_row:
    #         count = new_row.count(deposit)
    #         deposits[deposit] += count

commands = input().split(", ")

current_position = starting_position

for direction in commands:
    row = current_position[0] + directions[direction][0]
    col = current_position[1] + directions[direction][1]
    if col > 5 or col < 0:
        col = 6 - abs(col)
    if row > 5 or row < 0:
        row = 6 - abs(col)

    if field[row][col].isalpha():
        if field[row][col] == "R":
            print(f'Rover got broken at ({row}, {col})')
            break
        print(field[row][col], row, col)
    current_position = [row, col]


for x in field:
    print(x)

# TODO: not ready