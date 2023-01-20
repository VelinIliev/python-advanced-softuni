rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

# matrix = [[int(x) for x in input().split(", ")] for x in range(rows)]
# matrix = [list(map(int, input().split(", "))) for x in range(rows)]
sum_matrix = sum(map(sum, matrix))

print(sum_matrix)
print(matrix)
