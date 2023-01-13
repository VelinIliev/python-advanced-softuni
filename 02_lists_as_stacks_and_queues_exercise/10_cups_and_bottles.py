cups_capacity = [int(x) for x in input().split()]
bottles_capacity = [int(x) for x in input().split()]

wasted_water = 0
bottles_finished = False

while cups_capacity:

    if bottles_capacity:
        current_bottle = bottles_capacity.pop()
    else:
        bottles_finished = True
        break
    current_cup = cups_capacity.pop(0)

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup = current_cup - current_bottle
        cups_capacity.insert(0,current_cup)


if bottles_finished:
    cups_capacity = [str(x) for x in cups_capacity]
    print(f'Cups: {" ".join(cups_capacity)}')
else:
    bottles_capacity = [str(x) for x in bottles_capacity]
    print(f'Bottles: {" ".join(bottles_capacity)}')
print(f'Wasted litters of water: {wasted_water}')