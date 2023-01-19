size = int(input())

matrix = [[int(x) for x in input().split(" ")] for row in range(size)]

primary_diagonal = [(matrix[i][i]) for i in range(size)]
secondary_diagonal = [(matrix[i][abs(i - size + 1)]) for i in range(size)]

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)