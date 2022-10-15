def naughty_or_nice_list(*args, **kwargs):
    final_dict = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    kids = {}
    for x in args[0]:
        number = int(x[0])
        name = x[1]
        if number not in kids:
            kids[number] = [name]
        else:
            kids[number].append(name)
    print(kids)

    pass


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

#TODO:not ready