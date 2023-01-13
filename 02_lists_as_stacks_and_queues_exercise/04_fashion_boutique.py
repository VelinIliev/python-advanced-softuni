clothes_in_box = input().split(" ")
stack_of_clothes = [int(x) for x in clothes_in_box]
rack_capacity = int(input())

how_many_racks = 1
current_rack = 0

while stack_of_clothes:
    if current_rack + stack_of_clothes[-1] <= rack_capacity:
        current_rack += stack_of_clothes.pop()
    else:
        current_rack = 0
        how_many_racks += 1
print(how_many_racks)

