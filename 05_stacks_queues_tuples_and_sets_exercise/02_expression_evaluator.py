input_string = input().split(" ")

numbers = []

for char in input_string:
    if char != "-" and char != "+" and char != "/" and char != "*":
        numbers.append(int(char))
    elif char == "-":
        result = numbers.pop(0)
        for x in range(len(numbers)):
            result -= numbers.pop(0)
        numbers.insert(0, result)
    elif char == "*":
        result = numbers.pop(0)
        for x in range(len(numbers)):
            result *= numbers.pop()
        numbers.insert(0, result)
    elif char == "/":
        result = numbers.pop(0)
        for x in range(len(numbers)):
            result /= numbers.pop()
        numbers.insert(0, int(result))
    elif char == "+":
        result = numbers.pop(0)
        for x in range(len(numbers)):
            result += numbers.pop()
        numbers.insert(0, result)
print(*numbers)
