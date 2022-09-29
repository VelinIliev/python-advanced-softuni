kids = list(input().split(" "))
n = int(input())
index = n - 1

while len(kids) > 1:
    if index <= len(kids) - 1:
        print(f'Removed {kids[index]}')
        kids.pop(index)
        index += n - 1
    elif index > len(kids) - 1:
        index -= len(kids)

print(f'Last is {kids[0]}')
