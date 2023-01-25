def even_odd(*args):
    command = args[-1]
    numbers = [x for x in args if type(x) == int]
    operations = {
        'even': lambda x: [y for y in x if y % 2 == 0],
        'odd': lambda x: [y for y in x if y % 2 != 0],
    }
    return operations[command](numbers)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))