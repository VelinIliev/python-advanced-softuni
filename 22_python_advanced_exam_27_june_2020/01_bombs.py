bomb_effects = [int(x) for x in input().split(", ")]
bomb_casings = [int(x) for x in input().split(", ")]

bombs = {
    "Datura": 0,
    "Cherry": 0,
    "Smoke Decoy": 0
}
bomb_pouch = False

while bomb_effects and bomb_casings:
    effect = bomb_effects.pop(0)
    casing = bomb_casings.pop()
    sum_of_bomb = effect + casing
    if 40 <= sum_of_bomb < 60:
        bombs["Datura"] += 1
    elif 60 <= sum_of_bomb < 120:
        bombs["Cherry"] += 1
    elif sum_of_bomb >= 120:
        bombs["Smoke Decoy"] += 1
    else:
        bomb_casings.append(casing - 5)
    if bombs["Datura"] >= 3 and bombs["Cherry"] >= 3 and bombs["Smoke Decoy"] >= 3:
        bomb_pouch = True
        break

if bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f'Bomb Effects: {", ".join(str(x) for x in bomb_effects)}')
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f'Bomb Casings: {", ".join(str(x) for x in bomb_casings)}')
else:
    print('Bomb Casings: empty')
sorted_bombs = sorted(bombs.items())
for name, quantity in sorted_bombs:
    print(f'{name} Bombs: {quantity}')
