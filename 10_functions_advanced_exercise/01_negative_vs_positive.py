numbers = [int(x) for x in input().split()]


def negative_vs_positive(*args):
    negative = sum(list(filter(lambda x: (x < 0), args)))
    positive = sum(list(filter(lambda x: (x > 0), args)))
    stronger, weaker = ['negatives', 'positives'] if abs(negative) > positive else ['positives', 'negatives']

    return f'{negative}\n{positive}\n{f"The {stronger} are stronger than the {weaker}"}'


print(negative_vs_positive(*numbers))
