def even_odd_filter(**kwargs):
    numbers = {}
    if 'odd' in kwargs:
        numbers['odd'] = [x for x in kwargs['odd'] if x % 2 != 0]
    if 'even' in kwargs:
        numbers['even'] = [x for x in kwargs['even'] if x % 2 == 0]

    sorted_numbers = sorted(numbers.items(), key=lambda x: -len(x[1]))

    final_numbers = {}
    for k, v in sorted_numbers:
        final_numbers[k] = v
    return final_numbers


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
