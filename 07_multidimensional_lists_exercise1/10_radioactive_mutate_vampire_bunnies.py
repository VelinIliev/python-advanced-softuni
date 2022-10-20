rows, cols = [int(x) for x in input().split()]

matrix = []

directions = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0]
}
player_position = []
for row in range(rows):
    new_row = [x for x in input()]
    matrix.append(new_row)
    if "P" in new_row:
        player_position = [row, new_row.index("P")]

moves = input()
final_message = ""
game_over = False

for direction in moves:
    if game_over:
        break
    row = player_position[0] + directions[direction][0]
    col = player_position[1] + directions[direction][1]
    matrix[player_position[0]][player_position[1]] = "."
    if row in range(0, len(matrix)) and col in range(0, len(matrix[0])):
        if matrix[row][col] == ".":
            matrix[row][col] = "P"
            player_position = [row, col]
        elif matrix[row][col] == "B":
            final_message = f"dead: {row} {col}"
            game_over = True
    else:
        final_message = f'won: {player_position[0]} {player_position[1]}'
        game_over = True

    bunnies_positions = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == "B":
                bunnies_positions.append([x, y])
    for bunny in bunnies_positions:
        for side in directions:
            bunny_row = bunny[0] + directions[side][0]
            bunny_col = bunny[1] + directions[side][1]
            if bunny_row in range(0, len(matrix)) and bunny_col in range(0, len(matrix[0])):
                if matrix[bunny_row][bunny_col] == "P":
                    final_message = f"dead: {bunny_row} {bunny_col}"
                    game_over = True
                matrix[bunny_row][bunny_col] = "B"

for row in matrix:
    print("".join(row))
print(final_message)
