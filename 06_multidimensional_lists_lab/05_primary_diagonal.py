matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

sum_diagonal = 0

for row in range(matrix_size):
    sum_diagonal += matrix[row][row]

print(sum_diagonal)