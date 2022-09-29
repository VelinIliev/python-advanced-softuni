string = input()

stack = []
parentheses = []

for n, char in enumerate(string):
    if char == "(":
        stack.append(n)
    if char == ")":
        parentheses.append([stack.pop(), n+1])

for i in parentheses:
    start_index = i[0]
    end_index = i[1]
    print(string[start_index:end_index])

# parentheses = []
#
# for i in range(len(string)):
#     if string[i] == "(":
#         parentheses.append(i)
#     elif string[i] == ")":
#         start_index = parentheses.pop()
#         print(string[start_index: i + 1])