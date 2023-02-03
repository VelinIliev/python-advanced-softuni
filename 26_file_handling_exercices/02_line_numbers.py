from string import punctuation

with open('text.txt', 'r') as ff:
    first_file = ff.readlines()

with open('output.txt', 'w') as second_file:
    for line_number, line in enumerate(first_file, 1):
        count_letters = 0
        count_punctuation = 0
        for letter in line:
            if letter.isalpha():
                count_letters += 1
            elif letter in punctuation:
                count_punctuation += 1
        second_file.write(f'Line {line_number}: {line.strip()} ({count_letters})({count_punctuation})\n')
