numbers = input().split()
first_set_len = int(numbers[0])
second_set_len = int(numbers[1])

first_set = set()
second_set = set()

for number in range(first_set_len):
    new_number = input()
    first_set.add(new_number)
for number in range(second_set_len):
    new_number = input()
    second_set.add(new_number)

intersection = first_set & second_set
for number in intersection:
    print(number)