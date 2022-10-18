def list_manipulator(*args):
    list_of_numbers = args[0]
    command = args[1] + " " + args[2]
    others = args[3:]
    if command == "remove end":
        repetitions = 0
        if others:
            repetitions = others[0]
        else:
            repetitions = 1
        for _ in range(repetitions):
            if list_of_numbers:
                list_of_numbers.pop()
    elif command == "remove beginning":
        repetitions = 0
        if others:
            repetitions = others[0]
        else:
            repetitions = 1
        for _ in range(repetitions):
            if list_of_numbers:
                list_of_numbers.pop(0)
    elif command == "add beginning":
        list_of_numbers = [*others, *list_of_numbers]
    elif command == "add end":
        list_of_numbers = [*list_of_numbers, *others]
    return list_of_numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
