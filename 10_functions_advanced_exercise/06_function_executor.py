def func_executor(*args):
    return_result = []

    for func in args:
        function_to_execute = func[0]
        new_args = func[1]
        result = function_to_execute(*new_args)
        function_name = function_to_execute.__name__
        return_result.append(f'{function_name} - {result}')
    return "\n".join(return_result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn", )),
))
