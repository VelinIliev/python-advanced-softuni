working_bees = [int(x) for x in input().split()]
nectar = [int(x) for x in input().split()]
honey_making_process = input().split()

collected = 0

while working_bees and nectar:
    first_bee = working_bees[0]
    last_nectar = nectar[-1]
    if last_nectar >= first_bee:
        operation = honey_making_process.pop(0)
        if last_nectar > 0:
            if operation == "+":
                collected += abs(first_bee + last_nectar)
            elif operation == "-":
                collected += abs(first_bee - last_nectar)
            elif operation == "*":
                collected += abs(first_bee * last_nectar)
            elif operation == "/":
                collected += abs(first_bee / last_nectar)
        working_bees.pop(0)
        nectar.pop()
    else:
        nectar.pop()

print(f'Total honey made: {collected}')
if working_bees:
    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
