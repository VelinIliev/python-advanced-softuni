vowels = input().split()
consonants = input().split()

words = ["rose", "tulip", "lotus", "daffodil"]
found_letters = []
word_found = False
final_word = ""

while vowels and consonants:
    first_letter = vowels.pop(0)
    second_letter = consonants.pop()
    for word in words:
        if first_letter in word:
            found_letters.append(first_letter)
        if second_letter in word:
            found_letters.append(second_letter)
    for word in words:
        list_word = [x for x in word]
        if len(set(found_letters).intersection(set(list_word))) == len(set(list_word)):
            final_word = word
            word_found = True
            break
    if word_found:
        break

if word_found:
    print(f'Word found: {final_word}')
else:
    print(f'Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(x for x in vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(x for x in consonants)}')
