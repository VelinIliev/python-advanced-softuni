size = int(input())
field = [[x for x in input()] for row in range(size)]

moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
boundaries = range(0, len(field))
knight_attacks = []
removed_knights = 0

while True:
    for row in boundaries:
        for col in boundaries:
            possible_attacks = 0
            if field[row][col] != "K":
                continue
            for move in moves:
                move_row = row + move[0]
                move_col = col + move[1]
                if move_row in boundaries and move_col in boundaries \
                        and field[move_row][move_col] == "K":
                    possible_attacks += 1
            if possible_attacks > 0:
                knight_attacks.append([row, col, possible_attacks])

    if knight_attacks:
        knight_attacks.sort(key=lambda x: -x[2])
        row = knight_attacks[0][0]
        col = knight_attacks[0][1]
        field[row][col] = "0"
        knight_attacks = []
        removed_knights += 1
    else:
        break

print(removed_knights)
