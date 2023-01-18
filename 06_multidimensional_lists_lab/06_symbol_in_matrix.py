size = int(input())

matrix = [[x for x in input()] for row in range(size)]

search_symbol = input()

for row in range(size):
    if search_symbol in matrix[row]:
        print(f'({row}, {matrix[row].index(search_symbol)})')
        break
else:
    print(f'{search_symbol} does not occur in the matrix')