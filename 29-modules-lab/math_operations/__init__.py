def math_operations(line):
    n1, operator, n2 = line.split()
    operators = {
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '^': lambda x, y: x ** y,
    }
    print(f'{operators[operator](float(n1), float(n2)):.2f}')