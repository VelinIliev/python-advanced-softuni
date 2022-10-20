def naughty_or_nice_list(*args, **kwargs):
    kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    santa_list = args[0]
    for i in range(1, len(args)):
        number, name = args[i].split("-")
        number = int(number)
        count = 0
        for kid in santa_list:
            if kid[0] == number:
                count += 1
        if count == 1:
            for x, kid in enumerate(santa_list):
                if kid[0] == number:
                    kids[name].append(kid[1])
                    santa_list.pop(x)
    for name, key in kwargs.items():
        count = 0
        for kid in santa_list:
            if name == kid[1]:
                count += 1
        if count == 1:
            for y, kid in enumerate(santa_list):
                if name == kid[1]:
                    kids[key].append(name)
                    santa_list.pop(y)
                pass
    for x, name in santa_list:
        kids["Not found"].append(name)
    final_string = ""

    for type, names in kids.items():
        if names:
            if type != "Not found":
                final_string += f'{type}: {", ".join(names)}\n'
            else:
                final_string += f'{type}: {", ".join(names)}'
    return final_string


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
