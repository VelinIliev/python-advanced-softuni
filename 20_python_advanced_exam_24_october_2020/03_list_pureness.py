def best_list_pureness(*test):
    list_of_numbers = test[0]
    rotations = test[1]
    best_pureness = 0
    best_rotation = 0

    for rotation in range(rotations + 1):
        pureness = 0
        for i, num in enumerate(list_of_numbers):
            pureness += i * num
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        # print(pureness)
        # print(rotation)
        list_of_numbers.insert(0, list_of_numbers.pop())
    return f'Best pureness {best_pureness} after {best_rotation} rotations'

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
print()
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
print()
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
