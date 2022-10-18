customers = [int(x) for x in input().split(", ")]
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:
    first_customer = customers.pop(0)
    last_taxi = taxis.pop()
    if first_customer <= last_taxi:
        total_time += first_customer
    else:
        customers.insert(0, first_customer)

if customers:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers)}')
else:
    print("All customers were driven to their destinations")
    print(f'Total time: {total_time} minutes')