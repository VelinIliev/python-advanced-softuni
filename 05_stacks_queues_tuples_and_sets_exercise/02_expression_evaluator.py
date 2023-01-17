input_string = input().split(" ")

numbers = []

for char in input_string:
    if char not in '-+/*':
        numbers.append(int(char))
    else:
        result = numbers.pop(0)
        for _ in range(len(numbers)):
            result = eval(f'{result}{char}{numbers.pop()}')
        numbers.insert(0, int(result))

print(*numbers)
