rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

max_sum = 0
max_sub_matrix = []

for y in range(rows - 1):
    for x in range(columns - 1):
        sub_matrix = []
        sum_2x2 = 0
        for i in range(y, y + 2):
            row = []
            for j in range(x, x + 2):
                row.append(matrix[i][j])
            sum_2x2 += sum(row)
            sub_matrix.append(row)
        if max_sum < sum_2x2:
            max_sum = sum_2x2
            max_sub_matrix = sub_matrix

print(f'{" ".join(str(x) for x in max_sub_matrix[0])}')
print(f'{" ".join(str(x) for x in max_sub_matrix[1])}')
print(max_sum)
