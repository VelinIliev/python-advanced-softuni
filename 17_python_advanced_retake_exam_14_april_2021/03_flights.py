def flights(*args):
    data = list(args)
    destinations = {}
    while data:
        new_entry = data.pop(0)
        if new_entry == "Finish":
            break
        else:
            destination = new_entry
            passengers = int(data.pop(0))
            if destination not in destinations:
                destinations[destination] = 0
            destinations[destination] += passengers
    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
