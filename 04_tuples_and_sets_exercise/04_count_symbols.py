input_text = input()

letters = set(x for x in input_text)

occurrences = {}

for letter in letters:
    times = input_text.count(letter)
    occurrences[letter] = times

[print(f'{letter}: {times} time/s') for letter, times in sorted(occurrences.items())]
