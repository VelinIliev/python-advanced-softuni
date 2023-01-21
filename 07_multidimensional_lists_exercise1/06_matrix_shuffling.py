rows, columns = [int(x) for x in input().split()]

matrix = []
for row in range(rows):
    new_row = input().split()
    matrix.append(new_row)

while True:
    command = input()
    if command == "END":
        break
    swap, *indexes = [int(x) if x.isdigit() else x for x in command.split()]

    if swap == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes
        if row1 in range(rows) and row2 in range(rows) \
                and col1 in range(columns) and col2 in range(columns):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(" ". join(row)) for row in matrix]
            continue
    print("Invalid input!")
