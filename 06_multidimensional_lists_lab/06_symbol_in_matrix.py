size = int(input())

matrix = []
for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)

search_symbol = input()
found = False

for row in range(size):
    if found:
        break
    for column in range(size):
        if matrix[row][column] == search_symbol:
            print(f'({row}, {column})')
            found = True
            break


if not found:
    print(f'{search_symbol} does not occur in the matrix')