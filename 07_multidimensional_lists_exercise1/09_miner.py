size = int(input())
directions = input().split()

field = []

for _ in range(size):
    new_row = [x for x in input().split()]
    field.append(new_row)

current_position = []

for row in range(len(field)):
    for column in range(row):
        if field[row][column] == "s":
            current_position = [row, column]
print(current_position)

boundaries = range(0, size)

for direction in directions:
    neighbor = []
    row = current_position[0]
    column = current_position[1]
    if direction == "left":
        neighbor = [row, column - 1]
    elif direction == "right":
        neighbor = [row, column + 1]
    elif direction == "up":
        neighbor = [row - 1, column]
    elif direction == "down":
        neighbor = [row + 1, column]

    if neighbor and neighbor[0] in boundaries and neighbor[1] in boundaries:
        neighbor_row = neighbor[0]
        neighbor_column = neighbor[1]
        if field[neighbor_row][neighbor_column] == "*":
            field[neighbor_row][neighbor_column] = "s"
            current_position = [neighbor_row, neighbor_column]
        print()
        for x in field:
            print(x)
    # if neighbor in boundaries:
    #     if neighbor == "*":




