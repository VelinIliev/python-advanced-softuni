number_of_commands = int(input())

stack = []

map_functions = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}
for command in range(number_of_commands):
    entry = [int(x) for x in input().split()]
    map_functions[entry[0]](entry)

stack.reverse()
print(*stack, sep=", ")
