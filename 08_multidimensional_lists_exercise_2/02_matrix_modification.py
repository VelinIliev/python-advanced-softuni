size = int(input())

matrix = []

for row in range(size):
    new_row = [int(x) for x in input().split()]
    matrix.append(new_row)

while True:
    command = input()
    if command == "END":
        for row in matrix:
            print(" ".join(str(x) for x in row))
        break
    else:
        command = command.split()
        action = command[0]
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])
        boundaries_rows = range(0, len(matrix))
        boundaries_cols = range(0, len(matrix[0]))
        # print(row, col, value)

        if row in boundaries_rows and col in boundaries_cols:
            if action == "Add":
                matrix[row][col] += value
            elif action == "Subtract":
                matrix[row][col] -= value
        else:
            print(f'Invalid coordinates')

