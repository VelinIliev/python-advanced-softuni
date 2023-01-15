number_of_guests = int(input())

invited_guests = set(input() for _ in range(number_of_guests))
arrived_guests = set()

while True:
    guest = input()
    if guest == "END":
        break
    else:
        arrived_guests.add(guest)

not_arrived_guests = invited_guests.difference(arrived_guests)
print(len(not_arrived_guests))
[print(guest) for guest in sorted(not_arrived_guests)]
