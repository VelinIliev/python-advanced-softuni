# sequences = {
#     'First': set(int(x) for x in input().split()),
#     'Second': set(int(x) for x in input().split()),
# }
#
# number_of_lines = int(input())
#
# for line in range(number_of_lines):
#     action, sequence, *numbers = input().split()
#     numbers = [int(x) for x in numbers]
#     if action == "Add":
#         [sequences[sequence].add(number) for number in numbers]
#     elif action == "Remove":
#         [sequences[sequence].discard(number) for number in numbers]
#     else:
#         print(sequences['First'].issuperset(sequences['Second']))
#
# [print(*sorted(value), sep=", ") for value in sequences.values()]

# variant 2
sequences = {
    'First': set(int(x) for x in input().split()),
    'Second': set(int(x) for x in input().split()),
    'Subset': None
}
functions = {
    "Add": lambda x, y: [x.add(number) for number in y],
    "Remove": lambda x, y: [x.discard(number) for number in y],
    "Check": lambda x, y: print(sequences['First'].issuperset(sequences['Second']))
}
number_of_lines = int(input())

for line in range(number_of_lines):
    command, sequence, *numbers = input().split()
    functions[command](sequences[sequence], [int(x) for x in numbers])

[print(*sorted(value), sep=", ") for value in sequences.values() if value is not None]
