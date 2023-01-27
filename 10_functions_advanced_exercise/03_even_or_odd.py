def even_odd(*args):
    command = args[-1]
    operations = {
        'even': lambda x: [num for num in x[:-1] if num % 2 == 0],
        'odd': lambda x: [num for num in x[:-1] if num % 2 != 0],
    }
    return operations[command](args)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))