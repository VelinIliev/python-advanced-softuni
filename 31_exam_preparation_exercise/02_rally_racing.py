size = int(input())
car_number = input()

field = [[x for x in input().split()] for row in range(size)]
position = [0, 0]

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}
distance_traveled = 0


def find_exit(target_row, target_col):
    field[target_row][target_col] = '.'
    for row in range(size):
        if "T" in field[row]:
            target_row, target_col = row, field[row].index("T")
    field[target_row][target_col] = '.'
    return target_row, target_col


while True:
    direction = input()
    if direction == 'End':
        print(f'Racing car {car_number} DNF.')
        field[position[0]][position[1]] = "C"
        break

    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]

    if field[row][col] == '.':
        distance_traveled += 10
    elif field[row][col] == "T":
        distance_traveled += 30
        row, col = find_exit(row, col)
    elif field[row][col] == 'F':
        distance_traveled += 10
        field[row][col] = 'C'
        print(f'Racing car {car_number} finished the stage!')
        break

    position = [row, col]

print(f'Distance covered {distance_traveled} km.')
[print(''.join(row)) for row in field]
