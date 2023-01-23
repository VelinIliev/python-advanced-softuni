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

for _ in range(number_of_commands):
    row = current_position[0]
    col = current_position[1]
    action, direction, *info = input().split()
    if action == 'move':
        steps = int(info[0])
        new_row = row + directions[direction][0] * steps
        new_col = col + directions[direction][1] * steps
        if new_row in range(5) and new_col in range(5) and matrix[new_row][new_col] == '.':
            matrix[row][col] = "."
            matrix[new_row][new_col] = 'A'
            current_position = [new_row, new_col]
    elif action == 'shoot':
        row_c = row
        col_c = col
        while True:
            check_row = row_c + directions[direction][0]
            check_col = col_c + directions[direction][1]
            if check_row not in range(0, 5) or check_col not in range(0, 5):
                break
            if matrix[check_row][check_col] == ".":
                row_c = check_row
                col_c = check_col
            elif matrix[check_row][check_col] == "x":
                targets_hit.append([check_row, check_col])
                matrix[check_row][check_col] = "."
                break
    if len(targets_hit) == targets:
        print(f'Training completed! All {targets} targets hit.')
        break
else:
    print(f'Training not completed! {targets - len(targets_hit)} targets left.')

if targets_hit:
    [print(target) for target in targets_hit]