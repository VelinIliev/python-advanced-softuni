colors = input().split()

main_colors = []

while colors:
    if len(colors) > 1:
        first_substring = colors.pop(0)
        second_substring = colors.pop()
    else:
        first_substring = colors.pop()
        second_substring = ""

    new_color_v1 = first_substring + second_substring
    new_color_v2 = second_substring + first_substring

    if new_color_v1 == "red" or new_color_v1 == "yellow" or new_color_v1 == "blue" or\
            new_color_v1 == "orange" or new_color_v1 == "purple" or new_color_v1 == "green":
        main_colors.append(new_color_v1)
    elif new_color_v2 == "red" or new_color_v2 == "yellow" or new_color_v2 == "blue" or \
            new_color_v2 == "orange" or new_color_v2 == "purple" or new_color_v2 == "green":
        main_colors.append(new_color_v2)
    else:
        first_substring = first_substring[:-1]
        second_substring = second_substring[:-1]
        middle = int(len(colors) / 2)
        if first_substring != "":
            colors.insert(middle, first_substring)
        if second_substring != "":
            colors.insert(middle, second_substring)


for color in main_colors:
    if color == "orange":
        if "red" not in main_colors or "yellow" not in main_colors:
            main_colors.remove(color)
    if color == "purple":
        if "red" not in main_colors or "blue" not in main_colors:
            main_colors.remove(color)
    if color == "green":
        if "yellow" not in main_colors or "blue" not in main_colors:
            main_colors.remove(color)

print(main_colors)