rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for y in range(rows)]

[print(sum([matrix[row][column] for row in range(rows)])) for column in range(columns)]
