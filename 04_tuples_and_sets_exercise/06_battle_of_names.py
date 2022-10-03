number_of_lines = int(input())

even_set = set()
odd_set = set()

for row in range(1, number_of_lines + 1):
    name = input()
    sum_name = 0
    for letter in name:
        sum_name += ord(letter)
    final_sum = int(sum_name / row)
    if final_sum % 2 == 0:
        even_set.add(final_sum)
    else:
        odd_set.add(final_sum)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    result = even_set | odd_set
elif odd_sum > even_sum:
    result = odd_set - even_set
else:
    result = even_set ^ odd_set

final = []
for x in result:
    final.append(str(x))

print(", ".join(final))