bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = [int(x) for x in input().split(", ")]

while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.pop(0)
    if bowl == customer:
        continue
    elif bowl > customer:
        bowl -= customer
        bowls_of_ramen.append(bowl)
    elif customer > bowl:
        customer -= bowl
        customers.insert(0, customer)

if len(customers) == 0:
    print(f'Great job! You served all the customers.')
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(str(x) for x in bowls_of_ramen)}')
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f'Customers left: {", ".join(str(x) for x in customers)}')