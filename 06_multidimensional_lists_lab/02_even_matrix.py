rows = int(input())

matrix = []

# for row in range(rows):
#     new_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
#     matrix.append(new_row)
#
# print(matrix)

for i in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)
matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(matrix)