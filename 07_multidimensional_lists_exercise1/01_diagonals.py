size = int(input())

matrix = []

for _ in range(size):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

primary_diagonal = [[],[]]

for i in range(size):
    primary_diagonal[0].append(matrix[i][i])

primary_diagonal[1] = sum(primary_diagonal[0])

secondary_diagonal = [[],[]]

for i in range(size):
    secondary_diagonal[0].append(matrix[i][abs(i - size + 1)])

secondary_diagonal[1] = sum(secondary_diagonal[0])

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal[0])}. Sum: {primary_diagonal[1]}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal[0])}. Sum: {secondary_diagonal[1]}')