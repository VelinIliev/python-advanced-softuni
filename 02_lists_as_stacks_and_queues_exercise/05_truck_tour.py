number_of_pumps = int(input())

current_tank_litters = 0
pumps = []
for pump in range(number_of_pumps):
    data = input().split(" ")
    amount_of_petrol = int(data[0])
    distance_to_next_pump = int(data[1])

    current_tank_litters += amount_of_petrol
    current_tank_litters -= distance_to_next_pump
    pumps.append(current_tank_litters)

min_value = min(pumps)
min_index = pumps.index(min_value)
# print(pumps)
# print(min_index)
if min_value >= 0:
    print(min_index)
else:
    min_index += 1
    if min_index > number_of_pumps - 1:
        min_index -= (number_of_pumps - 1)
    print(min_index)