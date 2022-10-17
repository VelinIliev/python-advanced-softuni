player1, player2 = input().split(", ")

scoreboard = {
    "player1": {
        "name": player1,
        "score": 501,
        "throws": 0
    },
    "player2": {
        "name": player2,
        "score": 501,
        "throws": 0
    }
}

board = []
for row in range(7):
    new_row = [int(x) if x.isdigit() else x for x in input().split()]
    board.append(new_row)
counter = 0

while scoreboard["player1"]["score"] > 0 and scoreboard["player2"]["score"] > 0:
    counter += 1
    current_player = ""
    if counter % 2 != 0:
        current_player = "player1"
    else:
        current_player = "player2"
    scoreboard[current_player]["throws"] += 1

    coordinates = input().replace("(", "").replace(")", "").split(", ")
    row = int(coordinates[0])
    col = int(coordinates[1])

    if row in range(0, 7) and col in range(0, len(board[0]) - 1):
        if type(board[row][col]) == str:
            if board[row][col] == "B":
                print(f'{scoreboard[current_player]["name"]} won the game with {scoreboard[current_player]["throws"]} throws!')
                break
            elif board[row][col] == "D":
                points = (board[row][0] + board[row][len(board[0]) - 1] + board[0][col] + board[6][col]) * 2
                scoreboard[current_player]["score"] -= points
            elif board[row][col] == "T":
                points = (board[row][0] + board[row][len(board[0]) - 1] + board[0][col] + board[6][col]) * 3
                scoreboard[current_player]["score"] -= points
        elif type(board[row][col]) == int:
            scoreboard[current_player]["score"] -= board[row][col]

    if scoreboard[current_player]["score"] <= 0:
        print(f'{scoreboard[current_player]["name"]} won the game with {scoreboard[current_player]["throws"]} throws!')
        break

