size = int(input())

matrix = []

for row in range(size):
    new_row = [int(x) for x in input().split()]
    matrix.append(new_row)

boundaries_rows = range(0, len(matrix))
boundaries_cols = range(0, len(matrix[0]))

while True:
    command = input()
    if command == "END":
        break

    action, row, col, value = [int(x) if x.isdigit() else x for x in command.split()]
    if row not in boundaries_rows or col not in boundaries_cols:
        print(f'Invalid coordinates')
        continue

    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value


[print(" ".join(str(x) for x in row)) for row in matrix]