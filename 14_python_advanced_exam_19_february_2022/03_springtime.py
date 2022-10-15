def start_spring(**objects):
    elements = {}
    string_to_return = ""
    for name, type_of_element in objects.items():
        if type_of_element not in elements:
            elements[type_of_element] = [name]
        else:
            elements[type_of_element].append(name)
    sorted_elements = sorted(elements.items(), key=lambda x: (-len(x[1]), x[0]))
    for type_of, items in sorted_elements:
        string_to_return += f'{type_of}:\n'
        sorted_items = sorted(items)
        for item in sorted_items:
            string_to_return += f'-{item}\n'
    return string_to_return

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
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


