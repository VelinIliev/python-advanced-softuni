size = int(input())

field = []
alice_position = []
collected_tea = 0

for row in range(size):
    new_row = [int(x) if x.lstrip("-").isnumeric() else x for x in  input().split()]
    if "A" in new_row:
        alice_position = [row, new_row.index("A")]
    field.append(new_row)

boundaries = range(0, size)
tea_party = False

row = alice_position[0]
col = alice_position[1]
field[row][col] = "*"

while True:
    direction = input()
    if tea_party:
        break
    if direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    elif direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    if row in boundaries and col in boundaries:
        if type(field[row][col]) == int:
            collected_tea += field[row][col]
            field[row][col] = "*"
            if collected_tea >= 10:
                print('She did it! She went to the party.')
                tea_party = True
                break
        elif field[row][col] == "." or field[row][col] == "*":
            field[row][col] = "*"
        elif field[row][col] == "R":
            print("Alice didn't make it to the tea party.")
            field[row][col] = "*"
            break
    else:
        print("Alice didn't make it to the tea party.")
        break

for row in field:
    print(" ".join(str(x) for x in row))
