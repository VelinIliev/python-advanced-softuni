size = 8
chessboard = []
queens = []

directions =[[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

for row in range(size):
    new_row = input().split()
    chessboard.append(new_row)
    for col in range(len(new_row)):
        if chessboard[row][col] == "Q":
            queens.append([row, col])

winning_queens = []

for queen in queens:
    row, col = queen[0], queen[1]
    for direction in directions:
        check_position = [row, col]
        while check_position[0] in range(0, size) and check_position[1] in range(0, size):
            new_row = check_position[0] + direction[0]
            new_col = check_position[1] + direction[1]
            if new_row in range(0, size) and new_col in range(0, size):
                if chessboard[new_row][new_col] == "Q":
                    break
                if chessboard[new_row][new_col] == "K":
                    winning_queens.append(queen)
                    break
            check_position = [new_row, new_col]

if winning_queens:
    for position in winning_queens:
        print(position)
else:
    print(f'The king is safe!')