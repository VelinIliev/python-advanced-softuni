seats = input().split(", ")
first_sequence = [int(x) for x in input().split(", ")]
second_sequence = [int(x) for x in input().split(", ")]
taken_seats = []
# for _ in range(len(first_sequence)):
rotations = 0

while True:
    if rotations == 10:
        break
    if len(taken_seats) == 3:
        break
    rotations += 1
    first_number = first_sequence.pop(0)
    second_number = second_sequence.pop()
    sum_of_two_numbers = first_number + second_number
    letter = chr(sum_of_two_numbers)
    first_seat = str(first_number) + letter
    second_seat = str(second_number) + letter

    if (first_seat in seats or second_seat in seats) and \
            first_seat not in taken_seats and second_seat not in taken_seats:
        if first_seat in seats:
            taken_seats.append(first_seat)
            seats.remove(first_seat)
        if second_seat in seats:
            taken_seats.append(second_seat)
            seats.remove(second_seat)
    else:
        first_sequence.append(first_number)
        second_sequence.insert(0, second_number)

print(f'Seat matches: {", ".join(x for x in taken_seats)}')
print(f'Rotations count: {rotations}')
