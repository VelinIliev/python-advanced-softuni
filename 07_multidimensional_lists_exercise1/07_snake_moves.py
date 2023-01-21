rows, columns = [int(x) for x in input().split()]
start_string = input()

if rows in range(1, 13) and columns in range(1, 13) \
        and len(start_string) in range(1, 21) \
        and " " not in start_string:
    start_string *= 20
    new_row = []
    new_matrix = []
    for x in range(1, columns * rows + 1):
        new_row.append(start_string[x - 1])
        if x % columns == 0:
            new_matrix.append(new_row)
            new_row = []
    for n, row in enumerate(new_matrix, 1):
        if n % 2 == 0:
            print("".join(row[::-1]))
        else:
            print("".join(row))
