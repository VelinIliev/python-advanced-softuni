file = open('text.txt', 'r')


for e, line in enumerate(file):
    if e % 2 == 0 :
        new_line = []
        for word in line.split():
            word = word.replace('-', '@').replace(',', '@').replace('.', '@').replace('!', '@').replace('?', '@')
            new_line.append(word)
        print(*new_line[::-1])