size = int(input())

field = []
position = []
barrows = []
won = False
for row in range(size):
    new_row = [x for x in input()]
    field.append(new_row)
    if "S" in new_row:
        position = [row, new_row.index("S")]
    if "B" in new_row:
        barrows.append([row, new_row.index("B")])

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
food = 0
while True:
    direction = input()
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]

    if row in range(0, size) and col in range(0, len(field[0])):
        field[position[0]][position[1]] = "."
        if field[row][col] == "*":
            food += 1
            position = [row, col]
            field[row][col] = "S"
        elif field[row][col] == "B":
            field[row][col] = "."
            barrows.remove([row, col])
            position = [barrows[0][0], barrows[0][1]]
        else:
            position = [row, col]

    else:
        field[position[0]][position[1]] = "."
        break
    if food == 10:
        won = True
        break

if won:
    print(f'You won! You fed the snake.')
else:
    print(f'Game over!')
print(f"Food eaten: {food}")
for row in field:
    print("".join(row))