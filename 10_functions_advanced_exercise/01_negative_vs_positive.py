numbers = [int(x) for x in input().split()]


def negative_vs_positive(*args):
    negative = [x for x in args if x < 0]
    positive = [x for x in args if x > 0]
    sum_positives = sum(positive)
    sum_negatives = sum(negative)
    last = ""
    if abs(sum_negatives) > sum_positives:
        last = "The negatives are stronger than the positives"
    else:
        last = "The positives are stronger than the negatives"
    return f'{sum_negatives}\n{sum_positives}\n{last}'


print(negative_vs_positive(*numbers))


