from collections import deque

queue = deque()

while True:
    entry = input()
    if entry == "End":
        break
    elif entry == "Paid":
        for person in range(len(queue)):
            served_person = queue.popleft()
            print(served_person)
    else:
        queue.append(entry)

print(f'{len(queue)} people remaining.')

# queue = []
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     elif command == "Paid":
#         for person in range(len(queue)):
#             served_person = queue.pop(0)
#             print(served_person)
#     else:
#         queue.append(command)
#
# print(f'{len(queue)} people remaining.')
