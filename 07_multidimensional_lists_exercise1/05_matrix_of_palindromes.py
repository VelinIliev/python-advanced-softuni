rows, columns = [int(x) for x in input().split()]

for char in range(rows):
    row = []
    for char2 in range(columns):
        row.append(chr(97 + char) + chr(97 + char + char2) + chr(97 + char))
    print(" ".join(row))