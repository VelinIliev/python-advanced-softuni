size = 6
players = input().split(", ")

board = [[x for x in input().split()] for row in range(size)]
move = 0
skip_moves = []

while True:
    move += 1
    coordinates = input().split(", ")
    row_ = int(coordinates[0][1])
    col = int(coordinates[1][0])

    if move in skip_moves:
        pass
    elif board[row_][col] == 'E':
        print(f'{players[0]} found the Exit and wins the game!')
        break
    elif board[row_][col] == "T":
        print(f'{players[0]} is out of the game! The winner is {players[1]}.')
        break
    elif board[row_][col] == 'W':
        print(f'{players[0]} hits a wall and needs to rest.')
        skip_moves.append(move + 2)
    players[0], players[1] = players[1], players[0]

