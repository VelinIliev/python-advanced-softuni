# numbers = list(input().split(" "))
# stack = []
#
# for i in range(len(numbers)):
#     stack.append(numbers.pop())
#
# print(" ".join(stack))

print(*input().split(" ")[::-1], sep=" ")
