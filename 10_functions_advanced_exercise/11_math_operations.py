def math_operations(*args, **operations):
    count = 0
    for number in args:
        count += 1
        if count == 1:
            operations['a'] += number
        elif count == 2:
            operations['s'] -= number
        elif count == 3:
            if number == 0:
                continue
            operations['d'] /= number
        elif count == 4:
            operations['m'] *= number

        if count == 4:
            count = 0

    sorted_numbers = sorted(operations.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f'{key}: {value:.1f}' for key, value in sorted_numbers)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))


