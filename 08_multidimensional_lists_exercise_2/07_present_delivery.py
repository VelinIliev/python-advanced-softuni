number_of_presents = int(input())
neighborhood_size = int(input())
nice_kids = 0
neighborhood = []
santa_position = []
nice_kids_with_present = 0
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


def check_direction(row, col, direction):
    boundaries_rows = range(0, len(neighborhood))
    boundaries_cols = range(0, len(neighborhood[0]))
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]
    if new_row in boundaries_rows and new_col in boundaries_cols:
        return True


def cookies_time(row, col):
    presents = 0
    with_presents = 0
    for direction in directions.values():
        new_row = row + direction[0]
        new_col = col + direction[1]
        if neighborhood[new_row][new_col] == "X":
            presents += 1
        elif neighborhood[new_row][new_col] == "V":
            presents += 1
            with_presents += 1
        neighborhood[new_row][new_col] = "-"
    return presents, with_presents


def move_santa(row, col, direction):
    neighborhood[row][col] = "-"
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]
    presents = 0
    with_presents = 0
    if neighborhood[new_row][new_col] == "V":
        with_presents += 1
        presents += 1
    elif neighborhood[new_row][new_col] == "C":
        p, w = cookies_time(new_row, new_col)
        presents += p
        with_presents += w
    neighborhood[new_row][new_col] = "S"
    return [new_row, new_col], presents, with_presents


def final_output(number_of_presents, nice_kids, nice_kids_with_present):
    if number_of_presents <= 0 and nice_kids > nice_kids_with_present:
        print("Santa ran out of presents!")
    for row in neighborhood:
        print(" ".join(row))
    if nice_kids == nice_kids_with_present:
        print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
    else:
        no_presents = nice_kids - nice_kids_with_present
        print(f'No presents for {no_presents} nice kid/s.')


command = input()

while command != "Christmas morning":
    direction = command
    row = santa_position[0]
    col = santa_position[1]
    if check_direction(row, col, direction):
        santa_position, presents, with_presents = move_santa(row, col, direction)
        number_of_presents -= presents
        nice_kids_with_present += with_presents
    if number_of_presents <= 0:
        break
    command = input()

final_output(number_of_presents, nice_kids, nice_kids_with_present)
