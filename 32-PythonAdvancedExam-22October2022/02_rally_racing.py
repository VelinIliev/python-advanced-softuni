def find_exit(entry_row, entry_col):
    field[entry_row][entry_col] = '.'
    for row in range(size):
        if "T" in field[row]:
            exit_row, exit_col = row, field[row].index("T")
            break
    field[exit_row][exit_col] = '.'
    return [exit_row, exit_col]


size, car_number = int(input()), input()

field = [[x for x in input().split()] for row in range(size)]
row, col = 0, 0

directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
distance_traveled = 0

command = input()

while command != 'End':
    row += directions[command][0]
    col += directions[command][1]

    distance_traveled += 10

    if field[row][col] == "T":
        distance_traveled += 20
        row, col = find_exit(row, col)
    elif field[row][col] == 'F':
        print(f'Racing car {car_number} finished the stage!')
        break

    command = input()
else:
    print(f'Racing car {car_number} DNF.')

field[row][col] = "C"
print(f'Distance covered {distance_traveled} km.')
[print(*row, sep="") for row in field]
