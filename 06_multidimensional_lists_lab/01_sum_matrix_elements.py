rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for x in range(rows)]
sum_matrix = sum(map(sum, matrix))

print(sum_matrix)
print(matrix)