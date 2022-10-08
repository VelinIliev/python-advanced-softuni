list_to_flatten = input().split("|")

final_list = []

for i in range(len(list_to_flatten)):
    new_row = list_to_flatten[i].split()
    final_list.append(new_row)

final_list = final_list[::-1]

list_to_print = []
for row in final_list:
    for data in row:
        list_to_print.append(data)

print(" ".join(list_to_print))