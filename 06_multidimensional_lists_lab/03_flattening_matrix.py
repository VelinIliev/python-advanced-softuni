from functools import reduce

rows = int(input())

matrix = []

for row in range(rows):
    new_row = [int(x) for x in input().split(", ")]
    matrix.append(new_row)

# matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

matrix = reduce(lambda x, y: x + y, matrix)

print(matrix)
