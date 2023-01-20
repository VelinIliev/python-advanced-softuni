rows = int(input())

matrix = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(current_row)
# matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for x in range(rows)]

print(matrix)