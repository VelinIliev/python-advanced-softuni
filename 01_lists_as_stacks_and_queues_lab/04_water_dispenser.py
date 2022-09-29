from collections import deque

water_in_dispenser = int(input())

queue = deque()

while True:
    command = input()
    if command == "End":
        break
    elif command == "Start":
        pass
    elif command.startswith("refill"):
        command = command.split(" ")
        litters = int(command[1])
        water_in_dispenser += litters
    elif command.isdigit():
        litters = int(command)
        if water_in_dispenser - litters >= 0:
            served_person = queue.popleft()
            water_in_dispenser -= litters
            print(f"{served_person} got water")
        else:
            not_served_person = queue.popleft()
            print(f'{not_served_person} must wait')
    else:
        queue.append(command)

print(f'{water_in_dispenser} liters left')
