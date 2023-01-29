first_file = open('words.txt', 'r')

words = {

}
for line in first_file:
    for word in line.split():
        words[word] = 0


second_file = open('input.txt', 'r')

for line in second_file:
    for word in line.split():
        word = word.replace("-", "").replace(".", "").replace(",", "").replace("?", "").replace("!", "")
        word = word.lower()
        if word in words:
            words[word] += 1

sorted_file = list(sorted(words.items(), key=lambda x: -x[1]))


with open('output.txt', 'w') as f:
    for k, v in sorted_file:
        print(f"{k} - {v}")
        f.write(f"{k} - {v}\n")
