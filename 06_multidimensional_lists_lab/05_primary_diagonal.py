matrix_size = int(input())

matrix = []
for row in range(matrix_size):
    new_row = [int(x) for x in input().split(" ")]
    matrix.append(new_row)

diagonal_sum = 0
for row in range(matrix_size):
    diagonal_sum += matrix[row][row]

print(diagonal_sum)

# matrix = [[int(x) for x in input().split(" ")] for row in range(matrix_size)]
# print(sum([matrix[row][row] for row in range(matrix_size)]))
