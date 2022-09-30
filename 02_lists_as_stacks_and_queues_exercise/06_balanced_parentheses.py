string = list(input())

parentheses = []
stack = []

is_balanced = True

for char in string:
    if char == "{" or char == "(" or char == "[":
        stack.append(char)
    if char == "}" or char == ")" or char == "]":
        if len(stack) > 0:
            parentheses.append(stack.pop())
            parentheses.append(char)
        else:
            is_balanced = False
            break

# print(stack)
for i in range(len(parentheses)):
    if parentheses[i] == "{" and i < len(parentheses) - 2:
        if parentheses[i + 1] != "}":
            is_balanced = False
            break
    if parentheses[i] == "(" and i < len(parentheses) - 2:
        if parentheses[i + 1] != ")":
            is_balanced = False
            break
    if parentheses[i] == "[" and i < len(parentheses) - 2:
        if parentheses[i + 1] != "]":
            is_balanced = False
            break

if len(stack) > 0:
    is_balanced = False

if is_balanced:
    print("YES")
else:
    print("NO")