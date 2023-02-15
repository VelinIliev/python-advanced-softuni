seats = [x for x in input().split(", ")]
first_sequence = [int(x) for x in input().split(", ")]
second_sequence = [int(x) for x in input().split(", ")]

taken_seats = []
rotations = 0

while rotations != 10:
    if len(taken_seats) == 3:
        break
    rotations += 1

    first, second = first_sequence.pop(0),  second_sequence.pop()
    character = chr(first + second)
    first_seat = f'{first}{character}'
    second_seat = f'{second}{character}'
    if first_seat in seats and first_seat not in taken_seats:
        seats.remove(first_seat)
        taken_seats.append(first_seat)
    elif second_seat in seats and second_seat not in taken_seats:
        seats.remove(second_seat)
        taken_seats.append(second_seat)
    elif first_seat in taken_seats or second_seat in taken_seats:
        continue
    else:
        first_sequence.append(first)
        second_sequence.insert(0, second)


print(f"Seat matches: {', '.join(taken_seats)}")
print(f'Rotations count: {rotations}')