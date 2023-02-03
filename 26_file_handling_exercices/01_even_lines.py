symbols = ('-', ',', '.', '!', '?')

with open('text.txt', 'r') as file:
    text = file.readlines()
    for e, line in enumerate(text):
        if e % 2 != 0:
            continue
        for symbol in symbols:
            line = line.replace(symbol, "@")
        print(*line.split()[::-1])
