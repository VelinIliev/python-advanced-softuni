size = int(input())

matrix = []
for row in range(size):
    new_row = [int(x) for x in input().split(" ")]
    matrix.append(new_row)
# matrix = [[int(x) for x in input().split(" ")] for row in range(size)]

# primary_diagonal = sum([(matrix[i][i]) for i in range(size)])
# secondary_diagonal = sum([(matrix[i][abs(i - size + 1)]) for i in range(size)])
primary_diagonal = 0
secondary_diagonal = 0

for i in range(size):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][abs(i - size + 1)]


difference = abs(primary_diagonal - secondary_diagonal)

print(difference)