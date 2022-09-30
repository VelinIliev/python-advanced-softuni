from collections import deque
robots = input().split(";")
print(robots)

queue = deq

for robot in robots:
    data = robot.split("-")
    name = data[0]
    processing_time = int(data[1])
    print(name, processing_time)