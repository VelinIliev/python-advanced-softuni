size = int(input())

matrix = []
for row in range(size):
    new_row = [int(x) for x in input().split(" ")]
    matrix.append(new_row)
# matrix = [[int(x) for x in input().split(" ")] for row in range(size)]

# primary_diagonal = [(matrix[i][i]) for i in range(size)]
# secondary_diagonal = [(matrix[i][abs(i - size + 1)]) for i in range(size)]
primary_diagonal = []
for i in range(size):
    primary_diagonal.append(matrix[i][i])

secondary_diagonal = []
for i in range(size):
    secondary_diagonal.append(matrix[i][abs(i - size + 1)])


difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)