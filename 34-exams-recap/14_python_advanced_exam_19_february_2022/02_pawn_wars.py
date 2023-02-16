SIZE = 8

field = []
white_position = []
black_position = []
rows = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
cols = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}


for row in range(SIZE):
    new_row = [x for x in input().split()]
    if "b" in new_row:
        black_position = [row, new_row.index('b')]
    if "w" in new_row:
        white_position = [row, new_row.index('w')]
    field.append(new_row)

while True:
    w_row, w_col = white_position
    if w_row-1 in range(SIZE) and w_col-1 in range(SIZE) and field[w_row-1][w_col-1] == 'b':
        print(f'Game over! White win, capture on {cols[w_col-1]}{rows[w_row-1]}.')
        break
    if w_row-1 in range(SIZE) and w_col+1 in range(SIZE) and field[w_row-1][w_col+1] == 'b':
        print(f'Game over! White win, capture on {cols[w_col+1]}{rows[w_row-1]}.')
        break
    field[white_position[0]][white_position[1]] = "-"
    white_position[0] -= 1
    if white_position[0] == 0:
        print(f'Game over! White pawn is promoted to a queen at {cols[white_position[1]]}{rows[white_position[0]]}.')
        break
    field[white_position[0]][white_position[1]] = "w"

    b_row, b_col = black_position
    if b_row+1 in range(SIZE) and b_col-1 in range(SIZE) and field[b_row+1][b_col-1] == 'w':
        print(f'Game over! Black win, capture on {cols[b_col-1]}{rows[b_row+1]}.')
        break
    if b_row+1 in range(SIZE) and b_col+1 in range(SIZE) and field[b_row+1][b_col+1] == 'w':
        print(f'Game over! Black win, capture on {cols[b_col+1]}{rows[b_row+1]}.')
        break
    field[black_position[0]][black_position[1]] = "-"
    black_position[0] += 1
    if black_position[0] == 7:
        print(f'Game over! Black pawn is promoted to a queen at {cols[black_position[1]]}{rows[black_position[0]]}.')
        break
    field[black_position[0]][black_position[1]] = "b"
