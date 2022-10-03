number_of_usernames = int(input())

usernames = set()

for username in range(number_of_usernames):
    new_username = input()
    usernames.add(new_username)

for username in usernames:
    print(username)