def palindrome(word, index):
    if word[index] != word[-index - 1]:
        return f'{word} is not a palindrome'
    how_long = int(len(word) / 2)
    if how_long == index:
        return f'{word} is a palindrome'

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))

print(palindrome("peter", 0))