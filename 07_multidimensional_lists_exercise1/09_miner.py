size = int(input())
directions = input().split()

field = []

for row in range(size):
    new_row = [x for x in input().split()]
    field.append(new_row)

current_position = []
coal = 0
for row in range(len(field)):
    for column in range(size):
        if field[row][column] == "s":
            current_position = [row, column]
        elif field[row][column] == "c":
            coal += 1

boundaries = range(0, size)
game_ended = False

for direction in directions:
    if game_ended:
        break
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
            current_position = [neighbor_row, neighbor_column]
        elif field[neighbor_row][neighbor_column] == "c":
            field[neighbor_row][neighbor_column] = "*"
            coal -= 1
            current_position = [neighbor_row, neighbor_column]
            if coal == 0:
                game_ended = True
                print(f'You collected all coal! ({neighbor_row}, {neighbor_column})')
                break
        elif field[neighbor_row][neighbor_column] == "e":
            current_position = [neighbor_row, neighbor_column]
            game_ended = True
            print(f'Game over! ({neighbor_row}, {neighbor_column})')
            break

if not game_ended:
    print(f'{coal} pieces of coal left. ({current_position[0]}, {current_position[1]})')

# TODO: 90/100


