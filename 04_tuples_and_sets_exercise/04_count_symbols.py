input_text = input()

letters = set()
for letter in input_text:
    letters.add(letter)

occurrences = {}

for letter in letters:
    times = input_text.count(letter)
    occurrences[letter] = times
sorted_occurrences = sorted(occurrences.items())
for letter, times in sorted_occurrences:
    print(f'{letter}: {times} time/s')