matrix = []
current_position = []
targets_hit = []
targets = 0

for row in range(5):
    new_row = [x for x in input().split()]
    matrix.append(new_row)
    if "A" in new_row:
        col = new_row.index("A")
        current_position = [row, col]
    if "x" in new_row:
        targets += new_row.count('x')

directions = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}
number_of_commands = int(input())


def move(direction, steps):
    current_row = current_position[0] + directions[direction][0] * steps
    current_col = current_position[1] + directions[direction][1] * steps
    if current_row in range(5) and current_col in range(5) and matrix[current_row][current_col] == '.':
        matrix[current_position[0]][current_position[1]] = "."
        matrix[current_row][current_col] = 'A'
        return [current_row, current_col]
    else:
        return [current_position[0], current_position[1]]


def shoot(shoot_direction):
    current_row = current_position[0]
    current_col = current_position[1]
    while True:
        check_row = current_row + directions[shoot_direction][0]
        check_col = current_col + directions[shoot_direction][1]
        if check_row not in range(0, 5) or check_col not in range(0, 5):
            break
        if matrix[check_row][check_col] == ".":
            current_row = check_row
            current_col = check_col
        elif matrix[check_row][check_col] == "x":
            targets_hit.append([check_row, check_col])
            matrix[check_row][check_col] = "."
            break


for _ in range(number_of_commands):
    action, direction, *info = input().split()
    if action == 'move':
        steps = int(info[0])
        current_position = move(direction, steps)
    elif action == 'shoot':
        shoot(direction)

    if len(targets_hit) == targets:
        print(f'Training completed! All {targets} targets hit.')
        break
else:
    print(f'Training not completed! {targets - len(targets_hit)} targets left.')

if targets_hit:
    [print(target) for target in targets_hit]