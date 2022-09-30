from collections import deque
quantity_of_food = int(input())
orders = input().split(" ")
orders = [int(x) for x in orders]
queue = deque(orders)

biggest_order = max(queue)

for ordered_food in orders:
    if quantity_of_food - ordered_food >= 0:
        quantity_of_food -= ordered_food
        queue.popleft()
    else:
        break

if len(queue) == 0:
    print(biggest_order)
    print('Orders complete')
else:
    print(biggest_order)
    queue = [str(x) for x in queue]
    print(f"Orders left: {' '.join(queue)}")