size = int(input())

new_matrix = []

for row in range(size):
    new_row = [int(x) for x in input().split()]
    new_matrix.append(new_row)

coordinates = input().split()
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
boundaries = range(0, size)

for data in coordinates:
    bomb = [int(x) for x in data.split(",")]
    bomb_row = bomb[0]
    bomb_column = bomb[1]
    damage = new_matrix[bomb_row][bomb_column]
    if damage > 0:
        for direction in directions:
            row = bomb_row + direction[0]
            column = bomb_column + direction[1]
            if row in boundaries and column in boundaries \
                    and new_matrix[row][column] > 0:
                new_matrix[row][column] -= damage
        new_matrix[bomb_row][bomb_column] = 0

alive_cells = []
for row in range(len(new_matrix)):
    for column in range(len(new_matrix)):
        if new_matrix[row][column] > 0:
            alive_cells.append(new_matrix[row][column])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(" ".join([str(x) for x in row])) for row in new_matrix]
