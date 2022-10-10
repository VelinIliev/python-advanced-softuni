number_of_presents = int(input())
neighborhood_size = int(input())
nice_kids = 0
neighborhood = []
santa_position = []
directions = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

for row in range(neighborhood_size):
    new_row = input().split()
    neighborhood.append(new_row)
    if "S" in new_row:
        santa_position = [row, new_row.index("S")]
    if "V" in new_row:
        nice_kids += new_row.count("V")

boundaries_rows = range(0, len(neighborhood))
boundaries_cols = range(0, len(neighborhood[0]))
start_nice_kids = nice_kids

while True:
    command = input()
    if command == "Christmas morning":
        break
    else:
        direction = command
        next_row = santa_position[0] + directions[direction][0]
        next_col = santa_position[1] + directions[direction][1]
        if next_row in boundaries_rows and next_col in boundaries_cols:
            neighborhood[santa_position[0]][santa_position[1]] = "-"
            santa_position = [next_row, next_col]
            if neighborhood[next_row][next_col] == "C":
                for x in directions.values():
                    new_row = next_row + x[0]
                    new_col = next_col + x[1]
                    if neighborhood[new_row][new_col] == "V":
                        number_of_presents -= 1
                        nice_kids -= 1
                    elif neighborhood[new_row][new_col] == "X":
                        number_of_presents -= 1
                    neighborhood[new_row][new_col] = "-"
                    neighborhood[next_row][next_col] = "S"
                    if number_of_presents <= 0:
                        break
            elif neighborhood[next_row][next_col] == "V":
                number_of_presents -= 1
                nice_kids -= 1
                neighborhood[next_row][next_col] = "S"
                if number_of_presents <= 0:
                    break
            neighborhood[next_row][next_col] = "S"
    if nice_kids == 0:
        break
    # print()
    # for x in neighborhood:
    #     print(x)

if number_of_presents == 0:
    print('Santa ran out of presents!')
for x in neighborhood:
    print(" ".join(x))
if nice_kids:
    print(f'No presents for {nice_kids} nice kid/s.')
else:
    print(f'Good job, Santa! {start_nice_kids} happy nice kid/s.')

# print(nice_kids)

# TODO: not ready