materials = [int(x) for x in input().split()]
magic_level = [int(x) for x in input().split()]

ready_gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}
while materials and magic_level:
    last_material = materials[-1]
    first_magic_level = magic_level[0]
    sum_for_gift = last_material + first_magic_level

    if sum_for_gift < 100:
        if sum_for_gift % 2 == 0:
            last_material *= 2
            first_magic_level *= 3
            sum_for_gift = last_material + first_magic_level
        else:
            sum_for_gift *= 2
    if sum_for_gift > 499:
        sum_for_gift /= 2

    if 100 <= sum_for_gift <= 199:
        ready_gifts["Gemstone"] += 1
    elif 200 <= sum_for_gift <= 299:
        ready_gifts["Porcelain Sculpture"] += 1
    elif 300 <= sum_for_gift <= 399:
        ready_gifts["Gold"] += 1
    elif 400 <= sum_for_gift <= 499:
        ready_gifts["Diamond Jewellery"] += 1

    materials.pop()
    magic_level.pop(0)

if (ready_gifts["Gemstone"] > 0 and ready_gifts["Porcelain Sculpture"] > 0) or \
        (ready_gifts["Gold"] > 0 and ready_gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print(f'Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials)}')
if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')

sorted_gifts = sorted(ready_gifts.items())
for gift, quantity in sorted_gifts:
    if quantity > 0:
        print(f'{gift}: {quantity}')
