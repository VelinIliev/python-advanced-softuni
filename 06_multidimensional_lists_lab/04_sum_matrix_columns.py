rows, columns = [int(x) for x in input().split(", ")]

matrix = []
for row in range(rows):
    new_row = [int(x) for x in input().split()]
    matrix.append(new_row)

for col in range(columns):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)

# matrix = [[int(x) for x in input().split()] for y in range(rows)]
# [print(sum([matrix[row][column] for row in range(rows)])) for column in range(columns)]
