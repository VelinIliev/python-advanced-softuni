firework_effects = [int(x) for x in input().split(", ")]
explosive_power = [int(x) for x in input().split(", ")]

fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0
}
showtime = False

while firework_effects and explosive_power and not showtime:
    if firework_effects[0] <= 0:
        del firework_effects[0]
        continue
    if explosive_power[-1] <= 0:
        del explosive_power[-1]
        continue
    effect = firework_effects.pop(0)
    power = explosive_power.pop()
    mix_sum = effect + power
    if mix_sum % 3 == 0 and mix_sum % 5 == 0:
        fireworks["Crossette"] += 1
    elif mix_sum % 5 == 0:
        fireworks['Willow'] += 1
    elif mix_sum % 3 == 0:
        fireworks["Palm"] += 1
    else:
        firework_effects.append(effect - 1)
        explosive_power.append(power)
    if fireworks["Palm"] >= 3 and fireworks['Willow'] >= 3 \
            and fireworks['Crossette'] >= 3:
        showtime = True

if showtime:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f"Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f'Firework Effects left: {", ".join(str(x) for x in firework_effects)}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosive_power)}')

for firework, num in fireworks.items():
    print(f"{firework} Fireworks: {num}")
