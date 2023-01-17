sequences = {
    'First': set(int(x) for x in input().split()),
    'Second': set(int(x) for x in input().split()),
}

number_of_lines = int(input())

for line in range(number_of_lines):
    action, sequence, *numbers = input().split()
    numbers = [int(x) for x in numbers]
    if action == "Add":
        [sequences[sequence].add(number) for number in numbers]
    elif action == "Remove":
        [sequences[sequence].remove(number) for number in numbers if number in sequences[sequence]]
    else:
        print(sequences['First'].issuperset(sequences['Second']))

[print(*sorted(value), sep=", ") for value in sequences.values()]

# variant 2
# sequences = {
#     'First': set(int(x) for x in input().split()),
#     'Second': set(int(x) for x in input().split()),
#     'Subset': None
# }
# actions = {
#     "Add": lambda x: [x[0].add(number) for number in x[1]],
#     "Remove": lambda x: [x[0].remove(number) for number in x[1] if number in x[0]],
#     "Check": lambda x: print(sequences['First'].issuperset(sequences['Second']))
# }
# number_of_lines = int(input())
#
# for line in range(number_of_lines):
#     action, sequence, *numbers = input().split()
#     actions[action]([sequences[sequence], [int(x) for x in numbers]])
#
# [print(*sorted(value), sep=", ") for value in sequences.values() if value != None]
