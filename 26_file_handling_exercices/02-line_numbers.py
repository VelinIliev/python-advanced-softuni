file = open('text-02.txt', 'r')

with open('output-02.txt', 'w') as f:
    for n, line in enumerate(file, 1):
        count_letters = 0
        count_punctuation = 0
        for letter in line:
            if letter.isalpha():
                count_letters += 1
            elif letter in ".,-!?'":
                count_punctuation += 1
        f.write(f'Line {n}: {line.strip()} ({count_letters})({count_punctuation})\n')
file.close()
