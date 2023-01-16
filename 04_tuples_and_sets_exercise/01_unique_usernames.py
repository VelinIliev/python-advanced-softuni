number_of_usernames = int(input())

usernames = set(input() for _ in range(number_of_usernames))

[print(username) for username in usernames]
