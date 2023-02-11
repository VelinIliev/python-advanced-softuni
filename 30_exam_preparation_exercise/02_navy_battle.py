size = int(input())

field = []
position = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
count_hits = 0
count_mines = 0

for row in range(size):
    new_row = [x for x in input()]
    if "S" in new_row:
        position = [row, new_row.index("S")]
    field.append(new_row)


def move_submarine(row, col, target_row, target_col):
    field[row][col] = "-"
    field[target_row][target_col] = 'S'
    return [target_row, target_col]


while True:
    direction = input()
    row, col = position[0], position[1]
    target_row, target_col = row + directions[direction][0], col + directions[direction][1]

    if field[target_row][target_col] == '*':
        count_mines += 1
    elif field[target_row][target_col] == "C":
        count_hits += 1

    if count_mines == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{target_row}, {target_col}]!")
        break
    if count_hits == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    position = move_submarine(row, col, target_row, target_col)



