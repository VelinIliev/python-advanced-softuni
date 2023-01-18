rows = int(input())

matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for x in range(rows)]

print(matrix)