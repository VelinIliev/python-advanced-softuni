field = []
starting_position = []
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}
deposits = {
    "W": {
        "name": "Water",
        "quantity": 0,
        },
    "M": {
        "name": "Metal",
        "quantity": 0,
        },
    "C": {
        "name": "Concrete",
        "quantity": 0,
        },
}
for row in range(6):
    new_row = input().split()
    field.append(new_row)
    if "E" in new_row:
        starting_position = [row, new_row.index("E")]

commands = input().split(", ")

current_position = starting_position

for direction in commands:
    field[current_position[0]][current_position[1]] = "-"
    row = current_position[0] + directions[direction][0]
    col = current_position[1] + directions[direction][1]
    if col > 5 or col < 0:
        col = 6 - abs(col)
    if row > 5 or row < 0:
        row = 6 - abs(row)

    if field[row][col].isalpha():
        type_of_resource = field[row][col]
        if type_of_resource == "R":
            print(f'Rover got broken at ({row}, {col})')
            break
        else:
            deposit = deposits[type_of_resource]["name"]
            deposits[type_of_resource]["quantity"] += 1
            print(f'{deposit} deposit found at ({row}, {col})')
    current_position = [row, col]
    field[row][col] = "E"
    # print()
    # for x in field:
    #     print(x)


if deposits["W"]["quantity"] > 0 and deposits["C"]["quantity"] > 0 and deposits["M"]["quantity"] > 0:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')
