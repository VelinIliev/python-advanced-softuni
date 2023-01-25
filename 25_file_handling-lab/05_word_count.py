first_file = open('words.txt', 'r')

words = {

}
for line in first_file:
    for word in line.split():
        words[word] = 0

print(words)

second_file = open('input.txt', 'r')

for line in second_file:
    for word in line.split():
        word = word.replace("-", "")
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace("?", "")
        word = word.replace("!", "")
        word = word.lower()
        # print(word)
        if word in words:
            words[word] += 1

sorted_file = list(sorted(words.items(), key=lambda x: -x[1]))
print(sorted_file)


with open('output.txt', 'w') as f:
    for k, v in sorted_file:
        f.write(f"{k} - {v}\n")
