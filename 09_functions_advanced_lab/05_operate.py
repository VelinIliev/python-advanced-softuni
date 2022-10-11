def operate(operator, *args):

    def addition():
        return sum([x for x in args])

    def subtract():
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result

    def multiply():
        result = 1
        for num in args:
            result *= num
        return result

    def divide():
        result = args[0]
        for i in range(1, len(args)):
            if args[i] == 0:
                continue
            result /= args[i]
        return result

    if operator == "+":
        return addition()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("/", 10, 0, 4, 4))