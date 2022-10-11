def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

# multiply(2, 0, 1000, 5000)