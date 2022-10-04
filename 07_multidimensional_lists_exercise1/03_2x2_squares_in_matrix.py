rows, columns = [int(x) for x in input().split()]

matrix = []
count = 0

for _ in range(rows):
    row = input().split()
    matrix.append(row)

for x in range(rows - 1):
    for y in range(columns - 1):
        sub_matrix = set()
        for i in range(x, x + 2):
            for j in range (y, y + 2):
                sub_matrix.add(matrix[i][j])
        if len(sub_matrix) == 1:
            count += 1

print(count)