rows, columns = [int(x) for x in input().split()]

matrix = []
for row in range(rows):
    new_row = [int(x) for x in input().split()]
    matrix.append(new_row)

max_sum = -1000000
max_sub_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        sub_matrix = []
        sum_3x3 = 0
        for sub_row in range(row, row + 3):
            new_row = [matrix[sub_row][sub_column] for sub_column in range(column, column + 3)]
            sum_3x3 += sum(new_row)
            sub_matrix.append(new_row)
        if max_sum < sum_3x3:
            max_sum = sum_3x3
            max_sub_matrix = sub_matrix

print(f'Sum = {max_sum}')
[print(" ".join(str(x) for x in row)) for row in max_sub_matrix]