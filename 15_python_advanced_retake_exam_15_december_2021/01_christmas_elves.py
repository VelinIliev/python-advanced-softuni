elfs_energy = [int(x) for x in input().split()]
materials = [int(x) for x in input().split()]

energy_used = 0
number_of_toys = 0
counter = 0

while elfs_energy and materials:
    current_elf = elfs_energy.pop(0)
    if current_elf < 5:
        continue
    current_box = materials.pop()
    counter += 1
    if counter % 15 == 0:
        if current_elf >= current_box * 2:
            energy_used += current_box * 2
            current_elf -= current_box * 2
            elfs_energy.append(current_elf)
        else:
            current_elf *= 2
            elfs_energy.append(current_elf)
            materials.append(current_box)
    elif counter % 3 == 0:
        if current_elf >= current_box * 2:
            energy_used += current_box * 2
            current_elf -= current_box * 2
            number_of_toys += 2
            current_elf += 1
            elfs_energy.append(current_elf)
        else:
            current_elf *= 2
            elfs_energy.append(current_elf)
            materials.append(current_box)
    elif counter % 5 == 0:
        if current_elf >= current_box:
            energy_used += current_box
            current_elf -= current_box
            elfs_energy.append(current_elf)
        else:
            current_elf *= 2
            elfs_energy.append(current_elf)
            materials.append(current_box)
    elif current_elf >= current_box:
        energy_used += current_box
        current_elf -= current_box
        number_of_toys += 1
        current_elf += 1
        elfs_energy.append(current_elf)
    else:
        current_elf *= 2
        elfs_energy.append(current_elf)
        materials.append(current_box)
    # print(elfs_energy)
    # print(materials)

print(f'Toys: {number_of_toys}')
print(f'Energy: {energy_used}')
if elfs_energy:
    print(f'Elves left: {", ".join(str(x) for x in elfs_energy)}')
if materials:
    print(f'Boxes left: {", ".join(str(x) for x in materials)}')
