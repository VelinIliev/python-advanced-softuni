from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    ordered_food = orders[0]
    if quantity_of_food - ordered_food >= 0:
        quantity_of_food -= ordered_food
        orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break

if len(orders) == 0:
    print('Orders complete')
