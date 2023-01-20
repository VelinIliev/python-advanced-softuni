matrix_size = int(input())

matrix = []
for row in range(matrix_size):
    current_row = [int(x) for x in input().split(" ")]
    matrix.append(current_row)

# matrix = [[int(x) for x in input().split(" ")] for row in range(matrix_size)]

print(sum([matrix[row][row] for row in range(matrix_size)]))