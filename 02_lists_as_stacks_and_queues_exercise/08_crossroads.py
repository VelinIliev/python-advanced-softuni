from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
cars_passed = 0
queue = deque()
current_time = 0

no_crash = True
crash_symbol = ""
crash_car = ""

while no_crash:
    command = input()
    if command == "END":
        break
    elif command == "green":
        green_light = green_light_duration
        while green_light > 0:
            if queue:
                current_car = queue.popleft()
                for char in current_car:
                    green_light -= 1

                    if green_light == -free_window_duration - 1:
                        crash_symbol = char
                        crash_car = current_car
                if green_light >= 0:
                    cars_passed += 1
                else:
                    if green_light >= -free_window_duration:
                        cars_passed += 1
                    else:
                        no_crash = False
                        print("A crash happened!")
                        print(f"{crash_car} was hit at {crash_symbol}.")
                        break
            else:
                break
    else:
        queue.append(command)

if no_crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")