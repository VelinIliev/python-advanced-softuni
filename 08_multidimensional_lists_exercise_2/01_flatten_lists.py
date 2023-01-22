from functools import reduce

flatten_list = [[y for y in x.split()] for x in input().split("|")]
flatten_list = reduce(lambda x, y: x + y, flatten_list[::-1])

print(" ".join(flatten_list))