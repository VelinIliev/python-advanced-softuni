rows = int(input())

matrix = []
for i in range(rows):
    new_row = [int(x) for x in input().split(", ")]
    for j in new_row:
        matrix.append(j)

print(matrix)

# matrix = [map(int, input().split(", ")) for _ in range(rows)]
# print(matrix)
# flattened = [num for row in matrix for num in row]
# print(flattened)