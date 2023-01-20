size = int(input())

matrix = []
for row in range(size):
    new_row = [int(x) for x in input().split(", ")]
    matrix.append(new_row)
# matrix = [[int(x) for x in input().split(", ")] for row in range(size)]

primary_diagonal = [(matrix[i][i]) for i in range(size)]
secondary_diagonal = [(matrix[i][abs(i - size + 1)]) for i in range(size)]

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')