rows, cols = [int(x) for x in input().split(", ")]

matrix = []
position = []
decorations = 0
decorations_collected = 0
gifts = 0
gifts_collected = 0
cookies = 0
cookies_collected = 0

for row in range(rows):
    new_row = [x for x in input().split()]
    matrix.append(new_row)
    if "Y" in new_row:
        position = [row, new_row.index("Y")]
    if "D" in new_row:
        decorations += new_row.count("D")
    if "G" in new_row:
        gifts += new_row.count("G")
    if "C" in new_row:
        cookies += new_row.count("C")
directions = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0]
}
items_collected = False
while True:
    command = input()
    if command == "End":
        break
    else:
        command = command.split("-")
        direction = command[0]
        steps = int(command[1])
    for step in range(steps):
        row = position[0] + directions[direction][0]
        col = position[1] + directions[direction][1]
        if row > rows - 1 or row < 0:
            row = rows - abs(row)
        if col > cols - 1 or col < 0:
            col = cols - abs(col)
        matrix[position[0]][position[1]] = "x"
        if matrix[row][col] == "G":
            gifts -= 1
            gifts_collected += 1
        elif matrix[row][col] == "C":
            cookies -= 1
            cookies_collected += 1
        elif matrix[row][col] == "D":
            decorations -= 1
            decorations_collected += 1
        matrix[row][col] = "Y"
        position = [row, col]
        if gifts == 0 and decorations == 0 and cookies == 0:
            items_collected = True
            break
    if items_collected:
        break
    # print()
    # for x in matrix:
    #     print(x)

if items_collected:
    print(f'Merry Christmas!')
print(f"You've collected:")
print(f'- {decorations_collected} Christmas decorations')
print(f'- {gifts_collected} Gifts')
print(f'- {cookies_collected} Cookies')
for row in matrix:
    print(" ".join(row))
