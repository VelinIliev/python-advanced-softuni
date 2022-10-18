size = int(input())
number_of_bombs = int(input())

directions =[[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

field = []
for row in range(size):
    new_row = []
    for col in range(size):
        new_row.append(".")
    field.append(new_row)
for bomb in range(number_of_bombs):
    new_bomb = input().replace("(", "").replace(")", "").split(", ")
    row = int(new_bomb[0])
    col = int(new_bomb[1])
    field[row][col] = "*"

for row in range(size):
    for col in range(size):
        counter = 0
        if field[row][col] == ".":
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row in range(0, size) and new_col in range(0, size):
                    if field[new_row][new_col] == "*":
                        counter += 1
            field[row][col] = counter

for row in field:
    print(" ".join(str(x) for x in row))
