textiles = [int(x) for x in input().split()]
medicaments = [int(x) for x in input().split()]

healing_items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}

items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}
while textiles and medicaments:
    textile = textiles.pop(0)
    medicament = medicaments.pop()
    item = textile + medicament
    if item in healing_items:
        new_item = healing_items[item]
        items[new_item] += 1
    elif item > 100:
        items['MedKit'] += 1
        remainig = item - 100
        medicaments[-1] += remainig
    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
else:
    print('Textiles are empty.') if not textiles else print('Medicaments are empty.')

sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
for name, values in sorted_items:
    if values > 0:
        print(f'{name} - {values}')

if medicaments:
    print(f'Medicaments left: {", ".join(str(x) for x in medicaments[::-1])}')
if textiles:
    print(f'Textiles left: {", ".join(str(x) for x in textiles)}')