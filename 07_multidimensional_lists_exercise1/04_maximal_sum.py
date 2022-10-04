rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

max_sum = 0
max_sub_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        sub_matrix = []
        sum_3x3 = 0
        for sub_row in range(row, row + 3):
            new_row = []
            for sub_column in range(column, column + 3):
                new_row.append(matrix[sub_row][sub_column])
            sum_3x3 += sum(new_row)
            sub_matrix.append(new_row)
        if max_sum <= sum_3x3:
            max_sum = sum_3x3
            max_sub_matrix = sub_matrix

print(f'Sum = {max_sum}')
for row in max_sub_matrix:
    print(" ".join(str(x) for x in row))