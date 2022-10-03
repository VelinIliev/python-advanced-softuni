number_of_names = int(input())

unique_names = set()

for name in range(number_of_names):
    new_name = input()
    unique_names.add(new_name)

for name in unique_names:
    print(name)