caffeine_mg = [int(x) for x in input().split(", ")]
energy_drinks = [int(x) for x in input().split(", ")]
MAX_CAFFEINE = 300

total_caffeine = 0

while caffeine_mg and energy_drinks:
    current_caffeine_mg = caffeine_mg.pop()
    current_energy_drink = energy_drinks.pop(0)
    current_caffeine = current_caffeine_mg * current_energy_drink

    if total_caffeine + current_caffeine <= MAX_CAFFEINE:
        total_caffeine += current_caffeine
    else:
        energy_drinks.append(current_energy_drink)
        if total_caffeine - 30 < 0:
            total_caffeine = 0
        else:
            total_caffeine -= 30

if energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in energy_drinks)}')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')