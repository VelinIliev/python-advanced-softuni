vowels = input().split()
consonants = input().split()

words = ['rose', 'tulip', 'lotus', 'daffodil']
found_letters = []
found_word = False
word_is = ''

while vowels and consonants:
    if found_word:
        break
    vowel = vowels.pop(0)
    consonant = consonants.pop()
    for word in words:
        if vowel in word:
            found_letters.append(vowel)
        if consonant in word:
            found_letters.append(consonant)
        if all(x in found_letters for x in word):
            word_is = word
            found_word = True
            break

print(f'Word found: {word_is}') if found_word else print('Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')