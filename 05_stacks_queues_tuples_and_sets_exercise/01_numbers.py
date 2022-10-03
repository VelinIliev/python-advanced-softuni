first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

number_of_lines = int(input())

for line in range(number_of_lines):
    command = input().split()
    action = command[0]
    if action == "Add":
        sequence = command[1]
        # numbers = command[2::]
        numbers = [int(x) for x in command if x.isdigit()]
        if sequence == "First":
            for number in numbers:
                first_sequence.add(number)
        elif sequence == "Second":
            for number in numbers:
                second_sequence.add(number)
    elif action == "Remove":
        sequence = command[1]
        # numbers = command[2::]
        # numbers = set([int(x) for x in numbers])
        numbers = [int(x) for x in command if x.isdigit()]
        if sequence == "First":
            for number in numbers:
                if number in first_sequence:
                    first_sequence.remove(number)
        elif sequence == "Second":
            for number in numbers:
                if number in second_sequence:
                    second_sequence.remove(number)
    else:
        print(first_sequence.issuperset(second_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
