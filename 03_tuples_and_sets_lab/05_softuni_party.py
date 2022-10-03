number_of_guests = int(input())

first_list = set()

for guest in range(number_of_guests):
    new_guest = input()
    if len(new_guest) == 8:
        first_list.add(new_guest)

second_list = set()
while True:
    guest = input()
    if guest == "END":
        break
    else:
        if len(guest) == 8:
            second_list.add(guest)

guest_did_not_come = first_list.difference(second_list)
print(len(guest_did_not_come))
sorted_guests = sorted(guest_did_not_come)
for guest in sorted_guests:
    print(guest)
