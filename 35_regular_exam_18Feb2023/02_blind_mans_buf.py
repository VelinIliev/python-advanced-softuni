rows, cols = [int(x) for x in input().split()]

matrix = []
position = []
directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

for row in range(rows):
    new_row = input().split()
    if "B" in new_row:
        position = [row, new_row.index("B")]
    matrix.append(new_row)

touched_players = 0
moves = 0

while True:
    direction = input()
    if direction == "Finish":
        break

    new_row = position[0] + directions[direction][0]
    new_col = position[1] + directions[direction][1]

    if new_row not in range(rows) or new_col not in range(cols):
        continue
    elif matrix[new_row][new_col] == "O":
        continue
    elif matrix[new_row][new_col] == "P":
        touched_players += 1
        moves += 1
        position = [new_row, new_col]
        if touched_players == 3:
            break
    else:
        moves += 1
        position = [new_row, new_col]

print(f'Game over!')
print(f'Touched opponents: {touched_players} Moves made: {moves}')