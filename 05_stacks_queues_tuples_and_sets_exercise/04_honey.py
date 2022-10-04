working_bees = [int(x) for x in input().split()]
nectar = [int(x) for x in input().split()]
honey_making_process = input().split()

print(honey_making_process)
collected = 0
hive = []

while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar[-1]
    if current_nectar >= current_bee:
        working_bees.pop(0)
        hive.append(current_nectar)
        # nectar.pop()
    elif current_nectar < current_bee:
        nectar.pop()

print(collected)
# TODO: not ready