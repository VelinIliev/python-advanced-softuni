board = []
for row in range(6):
    new_row = [int(x) if x.isdigit() else x for x in input().split()]
    board.append(new_row)

score = 0
gift = ""

for x in range(3):
    data = input().split(", ")
    row = int(data[0].lstrip("("))
    col = int(data[1].rstrip(")"))
    if row in range(0, 6) and col in range(0, 6):
        if board[row][col] == "B":
            board[row][col] = 0
            for y in range(6):
                score += board[y][col]

if score < 100:
    needed_points = 100 - score
    print(f'Sorry! You need {needed_points} points more to win a prize.')
else:
    if 100 <= score <= 199:
        gift = "Football"
    elif 200 <= score <= 299:
        gift = "Teddy Bear"
    elif score >= 300:
        gift = "Lego Construction Set"
    print(f"Good job! You scored {score} points, and you've won {gift}.")