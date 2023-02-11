bowls_ramen = [int(x) for x in input().split(", ")]
customers = [int(x) for x in input().split(", ")]


while bowls_ramen and customers:
    ramen = bowls_ramen.pop()
    customer = customers.pop(0)
    if ramen == customer:
        continue
    elif ramen > customer:
        ramen -= customer
        bowls_ramen.append(ramen)
    elif customer > ramen:
        customer -= ramen
        customers.insert(0, customer)

if not customers:
    print('Great job! You served all the customers.')
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f'Customers left: {", ".join(str(x) for x in customers )}')