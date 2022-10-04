rows, columns = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix = 0

for row in range(rows):
    new_row = [int(x) for x in input().split(", ")]
    matrix.append(new_row)
    sum_matrix += sum(new_row)

print(sum_matrix)
print(matrix)