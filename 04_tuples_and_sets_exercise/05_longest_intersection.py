number_of_lines = int(input())

longest_intersection = 0
longest_intersection_content = []

for line in range(number_of_lines):
    first_half, second_half = input().split("-")

    first_start, first_end = map(lambda x: int(x), first_half.split(","))
    second_start, second_end = map(lambda x: int(x), second_half.split(","))

    first_set = set(x for x in range(first_start, first_end + 1))
    second_set = set(x for x in range(second_start, second_end + 1))

    intersection = first_set & second_set
    if len(intersection) > longest_intersection:
        longest_intersection = len(intersection)
        longest_intersection_content = [x for x in intersection]

print(f'Longest intersection is {longest_intersection_content} with length {longest_intersection}')