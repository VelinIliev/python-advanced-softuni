SIZE = 6

field = []
position = []

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
deposits = {'W': [0, 'Water'], 'M': [0, 'Metal'], 'C': [0, 'Concrete']}

for row in range(SIZE):
    new_row = [x for x in input().split()]
    if "E" in new_row:
        position = [row, new_row.index("E")]
    field.append(new_row)

commands = input().split(", ")

for direction in commands:
    position[0] += directions[direction][0]
    position[1] += directions[direction][1]

    for i in range(len(position)):
        if position[i] not in range(SIZE):
            position[i] = SIZE - abs(position[i])

    row_, col = position[0], position[1]

    if field[row_][col] in deposits:
        deposit = field[row_][col]
        print(f'{deposits[deposit][1]} deposit found at ({row_}, {col})')
        deposits[deposit][0] += 1
    elif field[row_][col] == "R":
        print(f'Rover got broken at ({row_}, {col})')
        break

if all(x[0] >= 1 for x in deposits.values()):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
