matrix_size = int(input())

matrix = [[int(x) for x in input().split(" ")] for row in range(matrix_size)]

print(sum([matrix[row][row] for row in range(matrix_size)]))