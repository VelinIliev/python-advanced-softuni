rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for row in range(rows)]
count = 0

for x in range(rows - 1):
    for y in range(columns - 1):
        sub_matrix = set([matrix[i][j] for j in range(y, y+2) for i in range(x, x + 2)])
        if len(sub_matrix) == 1:
            count += 1

print(count)