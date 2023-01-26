game_on = True
rows = 6
columns = 7
counter = 0
field = [[0 for row in range(columns)] for col in range(rows)]
[print(row) for row in field]


def player_move(player):
    finished = False
    move = input(f"{player}, please choose a column: ")
    while not finished:
        if move == 'e':
            break
        if not move.isdigit():
            print('Please enter a digit!')
        elif int(move) not in range(1, columns + 1):
            print("The column doesn't exist!")
            print("Try, again!")
        elif field[0][int(move) - 1] != 0:
            print('This column is full')
            print("Try, again!")
        else:
            print(move)
            break
        move = input(f"{player}, please choose a column: ")
    return move


def insert_player_move(player, move):
    column = move - 1
    player_sign = 1 if player == "Player 1" else 2
    for row in range(rows):
        if field[row][column] != 0:
            print(field[row][column])
            field[row - 1][column] = player_sign
            break
    else:
        field[rows - 1][column] = player_sign
    return [rows - 1, move]


def check_connections(row, col, player_sign):
    winner_found = False
    directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    for direction in directions:
        connections = 1
        check_row = row + direction[0]
        check_col = col + direction[1]
        while check_row in range(rows) and check_col in range(columns):
            if field[check_row][check_col] == player_sign:
                connections += 1
            check_row = check_row + direction[0]
            check_col = check_col + direction[1]
        if connections >= 4:
            winner_found = True
            break
    return winner_found


def check_for_winner(player):
    player_sign = 1 if player == "Player 1" else 2
    winner_found = False
    for row in range(rows):
        for col in range(columns):
            if field[row][col] == player_sign:
                winner_found = check_connections(row, col, player_sign)
    return winner_found


while game_on:
    counter += 1
    player = 'Player 1' if counter % 2 != 0 else "Player 2"

    move = player_move(player)

    if not move.isdigit():
        break

    position = insert_player_move(player, int(move))

    print()
    [print(row) for row in field]

    if check_for_winner(player):
        print()
        print(f'{player} wins the game!')
        print()
        new_game = input('Do you wanna to play another game? (y/n): ')
        if new_game.lower() == 'y':
            counter = 0
            field = [[0 for row in range(columns)] for col in range(rows)]
            [print(row) for row in field]
        else:
            game_on = False

