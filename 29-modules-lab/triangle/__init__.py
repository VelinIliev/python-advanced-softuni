def print_triangle(size):
    for row in range(1, size + 2):
        print(*[l for l in range(1, row)])
    for row in range(size, 0, -1):
        print(*[l for l in range(1, row)])


# print_triangle(5)