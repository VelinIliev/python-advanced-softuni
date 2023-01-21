size = int(input())
commands = input().split()
field = []
position = []
total_coal = 0

for row in range(size):
    new_row = input().split()
    field.append(new_row)
    if "s" in new_row:
        position = [row, new_row.index("s")]
    if "c" in new_row:
        total_coal += new_row.count("c")

boundaries_row = range(0, len(field))
boundaries_col = range(0, len(field[0]))
directions = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}
coal_collected = 0
game_over = False

for direction in commands:
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]
    if row in boundaries_row and col in boundaries_col:
        if field[row][col] == "c":
            coal_collected += 1
            field[row][col] = "*"
        elif field[row][col] == "e":
            print(f'Game over! ({row}, {col})')
            game_over = True
            break
        if coal_collected == total_coal:
            print(f'You collected all coal! ({row}, {col})')
            game_over = True
            break
        position = [row, col]

if not game_over:
    number_of_remaining_coal = total_coal - coal_collected
    print(f'{number_of_remaining_coal} pieces of coal left. ({position[0]}, {position[1]})')
