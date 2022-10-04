rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    new_row = [int(x) for x in input().split(" ")]
    matrix.append(new_row)

for column in range(columns):
    sum_column = 0
    for row in range(rows):
        sum_column += matrix[row][column]
    print(sum_column)