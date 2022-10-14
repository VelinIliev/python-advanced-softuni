chess_board = []
black_pawn_position = []
white_pawn_position = []
rows = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
cols = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}
for row in range(8):
    new_row = input().split()
    chess_board.append(new_row)
    if "b" in new_row:
        black_pawn_position = [row, new_row.index("b")]
    if "w" in new_row:
        white_pawn_position = [row, new_row.index("w")]

while True:
    row_white = white_pawn_position[0]
    col_white = white_pawn_position[1]
    if row_white > 0:
        chess_board[row_white][col_white] = "-"
        if col_white - 1 in range(0, 8) and chess_board[row_white - 1][col_white - 1] == "b":
            row_white = row_white - 1
            col_white = col_white - 1
            print(f'Game over! White win, capture on {cols[col_white]+rows[row_white]}.')
            chess_board[row_white][col_white] = "w"
            break
        elif col_white + 1 in range(0, 8) and chess_board[row_white - 1][col_white + 1] == "b":
            row_white = row_white - 1
            col_white = col_white + 1
            print(f'Game over! White win, capture on {cols[col_white] + rows[row_white]}.')
            chess_board[row_white][col_white] = "w"
            break
        else:
            row_white = row_white - 1
        chess_board[row_white][col_white] = "w"
        white_pawn_position = [row_white, col_white]
    if row_white == 0:
        print(f'Game over! White pawn is promoted to a queen at {cols[col_white]+rows[row_white]}.')
        break

    row_black = black_pawn_position[0]
    col_black = black_pawn_position[1]

    if row_black < 7:
        chess_board[row_black][col_black] = "-"
        if col_black - 1 in range(0, 8) and chess_board[row_black + 1][col_black - 1] == "w":
            row_black = row_black + 1
            col_black = col_black - 1
            print(f'Game over! Black win, capture on {cols[col_black] + rows[row_black]}.')
            chess_board[row_black][col_black] = "b"
            break
        elif col_black + 1 in range(0, 8) and chess_board[row_black + 1][col_black + 1] == "w":
            row_black = row_black - 1
            col_black = col_black + 1
            print(f'Game over! Black win, capture on {cols[col_black] + rows[row_black]}.')
            chess_board[row_black][col_black] = "b"
            break
        else:
            row_black = row_black + 1
        chess_board[row_black][col_black] = "b"
        black_pawn_position = [row_black, col_black]
    if row_black == 7:
        print(f'Game over! Black pawn is promoted to a queen at {cols[col_black] + rows[row_black]}.')
        break

#     print()
#     for x in chess_board:
#         print(x)
# print()
# for x in chess_board:
#     print(x)

# print(black_pawn_position)
# print(white_pawn_position)