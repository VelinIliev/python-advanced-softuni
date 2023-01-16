first_set_len, second_set_len = map(lambda x: int(x), input().split())

first_set = set(int(input()) for _ in range(first_set_len))
second_set = set(int(input()) for _ in range(second_set_len))

intersection = first_set & second_set
[print(number) for number in intersection]
