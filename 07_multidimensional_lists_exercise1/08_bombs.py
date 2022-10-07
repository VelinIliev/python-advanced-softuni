size = int(input())

new_matrix = []

for row in range(size):
    new_row = [int(x) for x in input().split()]
    new_matrix.append(new_row)

coordinates = input().split()

for data in coordinates:
    bomb = [int(x) for x in data.split(",")]
    bomb_row = bomb[0]
    bomb_column = bomb[1]
    damage = new_matrix[bomb_row][bomb_column]
    if damage > 0:
        boundaries = range(0, size)
        neighbors = [
            [bomb_row - 1, bomb_column],
            [bomb_row - 1, bomb_column + 1],
            [bomb_row, bomb_column + 1],
            [bomb_row + 1, bomb_column + 1],
            [bomb_row + 1, bomb_column],
            [bomb_row + 1, bomb_column - 1],
            [bomb_row, bomb_column - 1],
            [bomb_row - 1, bomb_column - 1]
        ]

        valid_neighbors = []
        for neighbor in neighbors:
            if neighbor[0] in boundaries and neighbor[1] in boundaries:
                valid_neighbors.append(neighbor)
        for neighbor in valid_neighbors:
            row = neighbor[0]
            column = neighbor[1]
            if new_matrix[row][column] > 0:
                new_matrix[row][column] -= damage

        new_matrix[bomb_row][bomb_column] = 0

alive_cells = []
for row in range(len(new_matrix)):
    for column in range(len(new_matrix)):
        if new_matrix[row][column] > 0:
            alive_cells.append(new_matrix[row][column])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in new_matrix:
    print(" ".join([str(x) for x in row]))
