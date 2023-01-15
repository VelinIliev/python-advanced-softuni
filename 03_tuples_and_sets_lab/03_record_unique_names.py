number_of_names = int(input())

unique_names = {input() for _ in range(number_of_names)}
# unique_names = set(input() for _ in range(number_of_names))

[print(name) for name in unique_names]
