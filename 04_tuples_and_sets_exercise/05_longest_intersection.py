number_of_lines = int(input())

longest_intersection = 0
longest_intersection_content = []

for line in range(number_of_lines):
    x = input().split("-")
    first_half = x[0].split(",")
    second_half = x[1].split(",")
    first_start = int(first_half[0])
    first_end = int(first_half[1])
    second_start = int(second_half[0])
    second_end = int(second_half[1])

    first_set = set()
    second_set = set()

    for x in range(first_start, first_end + 1):
        first_set.add(x)
    for x in range(second_start, second_end + 1):
        second_set.add(x)

    intersection = first_set & second_set
    if len(intersection) > longest_intersection:
        longest_intersection = len(intersection)
        longest_intersection_content = []
        for x in intersection:
            longest_intersection_content.append(x)

print(f'Longest intersection is {longest_intersection_content} with length {longest_intersection}')