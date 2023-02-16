def start_spring(**kwargs):
    springs = {}
    for name, type_ in kwargs.items():
        if type_ not in springs:
            springs[type_] = []
        springs[type_].append(name)

    output = []
    sorted_springs = sorted(springs.items(), key=lambda x: (-len(x[1]), x[0]))
    for type_, values in sorted_springs:
        output.append(f'{type_}:')
        [output.append(f'-{name}') for name in sorted(values)]

    return '\n'.join(output)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
