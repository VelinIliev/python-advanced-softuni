rows, columns = [int(x) for x in input().split()]

for char in range(rows):
    row = [chr(97 + char) + chr(97 + char + char2) + chr(97 + char) for char2 in range(columns)]

    print(" ".join(row))