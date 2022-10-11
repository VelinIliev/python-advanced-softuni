def concatenate(*args, **kwargs):
    new_string = ""
    for substring in args:
        new_string += substring
    for old_substring, new_substring in kwargs.items():
        new_string = new_string.replace(old_substring, new_substring)
    return new_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))