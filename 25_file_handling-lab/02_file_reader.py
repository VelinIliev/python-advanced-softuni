file = open('numbers.txt', 'r')

sum_numbers = 0
for line in file:
    sum_numbers += int(line)
file.close()
print(sum_numbers)