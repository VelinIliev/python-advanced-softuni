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
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


queue = deque()
# working robots
working = []
# queue of elements to be processed
elements = deque()

# starting queue of robots
for robot in robots:
    data = robot.split("-")
    name = data[0]
    processing_time = int(data[1])
    queue.append([name, processing_time])

# preparing queue of elements
while True:
    command = input()
    if command == "End":
        break
    else:
        element = command
        elements.append(element)

# processing_line
while len(elements) > 0:
    current_time += 1
    # check for free robot
    for i, robot in enumerate(working):
        if robot[2] == current_time:
            queue.append(working.pop(i))
    # assigning tasks to free robots
    if len(queue) > 0:
        current_robot = queue.popleft()
        name = current_robot[0]
        processing_time = current_robot[1]
        starting_time = convert_seconds_to_hh_mm_ss(current_time)
        current_element = elements.popleft()
        end_time = current_time + processing_time
        print(f'{name} - {current_element} [{starting_time}]')
        working.append([name, processing_time, end_time])
    # rotating pending elements
    else:
        not_processed_element = elements.popleft()
        elements.append(not_processed_element)