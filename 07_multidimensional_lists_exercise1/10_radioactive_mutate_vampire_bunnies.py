rows, cols = [int(x) for x in input().split()]

matrix = []
player_position = []
bunnies_positions = []

directions = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [1, 0],
    "D": [-1, 0]
}

for row in range(rows):
    new_row = [x for x in input()]
    if "P" in new_row:
        player_position = [row, new_row.index("P")]

    matrix.append(new_row)

for x in matrix:
    print(x)
print(player_position)
print(bunnies_positions)

#TODO: not ready