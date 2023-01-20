size = int(input())

matrix = []

for row in range(size):
    new_row = [x for x in input()]
    matrix.append(new_row)

search_symbol = input()

is_found = False

for row in range(size):
    if is_found:
        break
    for col in range(size):
        if matrix[row][col] == search_symbol:
            print(f'({row}, {col})')
            is_found = True
            break

if not is_found:
    print(f'{search_symbol} does not occur in the matrix')