size = int(input())

field = []
position = []

for row in range(size):
    new_row = [int(x) if x.isdigit() else x for x in input().split()]
    field.append(new_row)
    if "P" in new_row:
        position = [row, new_row.index("P")]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

coins = 0
moves = [position]
hit_wall = False

while coins < 100:
    direction = input()
    field[position[0]][position[1]] = 0
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]
    if row < 0 or row > len(field) - 1:
        row = size - abs(row)
    if col < 0 or col > len(field[0]) - 1:
        col = size - abs(col)

    if field[row][col] == "X":
        hit_wall = True
        moves.append([row, col])
        break
    else:
        coins += field[row][col]
        position = [row, col]
        moves.append([row, col])
    # print(row, col)

if coins >= 100 and not hit_wall:
    print(f"You won! You've collected {coins} coins.")
else:
    coins = int(coins / 2)
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for move in moves:
    print(move)