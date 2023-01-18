from functools import reduce

rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]
matrix = reduce(lambda x, y: x + y, matrix)

print(matrix)
