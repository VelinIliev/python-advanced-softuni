from functools import reduce


def operate(operator, *args):

    def addition():
        return reduce(lambda x, y: x + y, args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def multiply():
        return reduce(lambda x, y: x * y, args)

    def divide():
        list_args = [x for x in args if x != 0]
        return reduce(lambda x, y: x / y, list_args)

    operators = {
        "+": addition(),
        "-": subtract(),
        "*": multiply(),
        '/': divide(),
    }
    return operators[operator]


print(operate("/", 10, 0, 4, 4))
print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))