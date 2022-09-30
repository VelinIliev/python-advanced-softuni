number_of_commands = int(input())

stack = []

for command in range(number_of_commands):
    entry = input().split(" ")
    # print(entry)
    action = entry[0]
    if action == "1":
        number = int(entry[1])
        stack.append(number)
    elif action == '2':
        if len(stack) > 0:
            stack.pop()
    elif action == '3':
        if len(stack) > 0:
            print(max(stack))
    elif action == '4':
        if len(stack) > 0:
            print(min(stack))
    # print(stack)

stack = [str(x) for x in stack]
stack.reverse()
print(", ".join(stack))
