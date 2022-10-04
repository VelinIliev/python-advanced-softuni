materials = [int(x) for x in input().split()]
magic_level = [int(x) for x in input().split()]

presents = {}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.pop(0)
    total_magic_level = magic * material

    if total_magic_level == 400:
        toy = "Bicycle"
        if toy not in presents:
            presents[toy] = 0
        presents[toy] += 1
    elif total_magic_level == 300:
        toy = "Teddy bear"
        if toy not in presents:
            presents[toy] = 0
        presents[toy] += 1
    elif total_magic_level == 250:
        toy = "Wooden train"
        if toy not in presents:
            presents[toy] = 0
        presents[toy] += 1
    elif total_magic_level == 150:
        toy = "Doll"
        if toy not in presents:
            presents[toy] = 0
        presents[toy] += 1
    elif total_magic_level < 0:
        new_material = magic + material
        materials.append(new_material)
    elif total_magic_level > 0:
        material += 15
        materials.append(material)
    elif total_magic_level == 0:
        if material == 0 and magic == 0:
            continue
        elif material == 0:
            magic_level.insert(0, magic)
        elif magic == 0:
            materials.append(material)

if "Doll" in presents and "Wooden train" in presents or \
        "Teddy bear" in presents and "Bicycle" in presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print(f'No presents this Christmas!')

if materials:
    materials = reversed(materials)
    print(f'Materials left: {", ".join(str(x) for x in materials)}')
if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')

presents = sorted(presents.items())

for data in presents:
    present = data[0]
    count = data[1]
    print(f'{present}: {count}')