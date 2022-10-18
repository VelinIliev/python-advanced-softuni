def get_magic_triangle(rows):
    magic_triangle = [[1], [1, 1]]
    for row in range(2, rows):
        # magic_triangle.append([1, magic_triangle[row - 1], 1])
        new_row = []
        # print(len(magic_triangle[row - 1]) - 1)
        for i in range(len(magic_triangle[row - 1])):
            if i + 1 <= len(magic_triangle[row - 1]) - 1:
                new_row.append(magic_triangle[row - 1][i] + magic_triangle[row - 1][i + 1])
            else:
                break
        magic_triangle.append([1, *new_row, 1])
    return magic_triangle

get_magic_triangle(7)