numbers = tuple(map(float, input().split()))

numbers_and_occurrences = {}

for number in numbers:
    if number not in numbers_and_occurrences:
        numbers_and_occurrences[number] = 0
    numbers_and_occurrences[number] += 1

for number, occurrences in numbers_and_occurrences.items():
    print(f'{number:.1f} - {occurrences} times')