rows, columns = [int(x) for x in input().split()]

matrix = []
for row in range(rows):
    new_row = input().split()
    matrix.append(new_row)
# matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    else:
        swap, *indexes = [int(x) if x.isdigit() else x for x in command.split()]

        if swap == "swap" and len(indexes) == 4:
            row1, col1, row2, col2 = indexes
            if rows >= row1 >= 0 and rows >= row2 >= 0 and columns >= col1 >= 0 and columns >= col2 >= 0:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for row in matrix:
                    print(" ". join(row))
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
