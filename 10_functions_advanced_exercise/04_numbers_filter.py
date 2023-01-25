def even_odd_filter(**kwargs):

    numbers = {}
    if 'odd' in kwargs:
        numbers['odd'] = list(filter(lambda x: x % 2 != 0, kwargs['odd']))
    if 'even' in kwargs:
        numbers['even'] = list(filter(lambda x: x % 2 == 0, kwargs['even']))
    sorted_numbers = sorted(numbers.items(), key=lambda x: -len(x[1]))
    return dict(sorted_numbers)


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
