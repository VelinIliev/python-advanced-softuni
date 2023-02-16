def words_sorting(*args):
    output = []
    words = {word: sum([ord(x) for x in word]) for word in args}
    sum_v = sum(x for x in words.values())
    sorted_words = sorted(words.items()) if sum_v % 2 == 0 else sorted(words.items(), key=lambda x: -x[1])
    [output.append(f'{word} - {value}') for word, value in sorted_words]
    return "\n".join(output)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
