players = {}
positions = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


def print_field(field):
    [print(f'| {" | ".join(str(x) for x in row)} |') for row in field]
    print()


def initialisation():
    # players = {}
    player1 = input("Player one name: ")
    player2 = input("Player two name: ")

    player1_sign = input(f'{player1} would you like to play with "X" or "O"? ')
    while player1_sign not in 'xXoO':
        player1_sign = input(f'{player1} would you like to play with "X" or "O"? ')
    player2_sign = 'X' if player1_sign.upper() == "O" else "O"

    players['player1'] = {'name': player1, 'sign': player1_sign.upper()}
    players['player2'] = {'name': player2, 'sign': player2_sign}

    field_numeration = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print()
    print('This is the numeration of the board:')
    print_field(field_numeration)

    field = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    return field


def is_position_taken(position, field):
    row = positions[position][0]
    col = positions[position][1]
    if field[row][col] != " ":
        return True
    return False


def choose_position(player, field):
    print_field(field)
    position = input(f'{player["name"]} choose a free position [1 - 9]: ')
    while True:
        if not position.isdigit():
            print("Please enter a number")
        elif int(position) not in positions:
            print("Please enter a valid position")
        elif is_position_taken(int(position), field):
            print("Please enter a free position")
        else:
            break
        position = input(f'{player["name"]} choose a free position [1 - 9]: ')
    return int(position)


def modify_field(position, field, player):
    row = positions[position][0]
    col = positions[position][1]
    field[row][col] = player['sign']
    return field


def check_for_victory(field, player):
    player_sign = player['sign']
    directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] == player_sign:
                for direction in directions:
                    count = 1
                    check_row = row + direction[0]
                    check_col = col + direction[1]
                    while check_row in range(3) and check_col in range(3):
                        if field[check_row][check_col] == player_sign:
                            count += 1
                        check_row = check_row + direction[0]
                        check_col = check_col + direction[1]
                    if count >= 3:
                        return True
    return False


def main():
    field = initialisation()
    counter = 0
    game_is_on = True

    while game_is_on:
        counter += 1
        player = players['player1'] if counter % 2 != 0 else players['player2']
        position = choose_position(player, field)
        field = modify_field(position, field, player)
        if check_for_victory(field, player):
            print(f"{player['name']} won!")
            new_game = input("Do you wanna new game? [y/n]: ")
            while True:
                if new_game.lower() in 'yn':
                    break
                new_game = input("Do you wanna new game? [y/n]: ")
            if new_game.lower() == 'n':
                break
            counter = 0
            field = initialisation()

main()