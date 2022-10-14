def words_sorting(*args):
    words = {}
    for word in args:
        ascii_sum = 0
        for char in word:
            ascii_sum += ord(char)
        words[word] = ascii_sum

    keys_sum = 0
    for value in words.values():
        keys_sum += value

    if keys_sum % 2 == 0:
        sorted_words = sorted(words.items(), key=lambda x: x[0])
    else:
        sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)

    return_string = ""
    for x in sorted_words:
        return_string += f'{x[0]} - {x[1]}\n'
    return return_string


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
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
