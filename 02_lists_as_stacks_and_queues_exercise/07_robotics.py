from collections import deque

robots = input().split(";")
starting_time = input().split(":")

# convert hours / minutes to seconds
starting_time = [int(x) for x in starting_time]
current_time = starting_time[0] * 3600 + starting_time[1] * 60 + starting_time[2]


def convert_seconds_to_hh_mm_ss(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = (seconds - hours * 3600 - minutes * 60)
    while hours > 23:
        hours -= 24
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


# queue of elements to be processed
elements = deque()

# starting queue of robots
for i, robot in enumerate(robots):
    data = robot.split("-")
    name = data[0]
    processing_time = int(data[1])
    robots[i] = [name, processing_time, current_time]

# starting queue of elements
while True:
    command = input()
    if command == "End":
        break
    else:
        element = command
        elements.append(element)

# processing elements
while elements:
    current_time += 1
    current_product = elements.popleft()
    # assigning tasks to free robots
    for current_robot in robots:
        end_time = int(current_robot[2])
        if end_time <= current_time:
            name = current_robot[0]
            processing_time = int(current_robot[1])
            starting_time = convert_seconds_to_hh_mm_ss(current_time)
            end_time = current_time + processing_time
            print(f'{name} - {current_product} [{starting_time}]')
            current_robot[2] = end_time
            break
    # rotating pending elements
    else:
        elements.append(current_product)
