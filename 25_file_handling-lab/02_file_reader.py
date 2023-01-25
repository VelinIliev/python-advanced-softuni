file = open('numbers.txt', 'r')

sum = 0
for line in file:
    sum += int(line)

print(sum)