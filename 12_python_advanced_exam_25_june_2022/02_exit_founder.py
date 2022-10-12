names = input().split(", ")
first_player = names[0]
second_player = names[1]

matrix = []

for row in range(6):
    new_row = [x for x in input().split()]
    matrix.append(new_row)

move = 0
players_to_rest = []

while True:
    current_player = ""
    other_player = ""
    move += 1
    if move % 2 == 0:
        current_player = second_player
        other_player = first_player
    else:
        current_player = first_player
        other_player = second_player
    coordinate = list(int(x) for x in input() if x.isnumeric())
    row = coordinate[0]
    col = coordinate[1]
    if current_player in players_to_rest:
        players_to_rest.remove(current_player)
        continue
    elif matrix[row][col] == "E":
        print(f'{current_player} found the Exit and wins the game! ')
        break
    elif matrix[row][col] == "T":
        print(f'{current_player} is out of the game! The winner is {other_player}.')
        break
    elif matrix[row][col] == "W":
        print(f'{current_player} hits a wall and needs to rest.')
        players_to_rest.append(current_player)

# for x in matrix:
#     print(x)
