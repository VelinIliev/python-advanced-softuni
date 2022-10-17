pizzas = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]
pizzas_made = 0

while pizzas and employees:
    first_pizza = pizzas.pop(0)
    if first_pizza <= 0 or first_pizza > 10:
        continue
    last_employee = employees.pop()
    if first_pizza <= last_employee:
        pizzas_made += first_pizza
    else:
        pizzas.insert(0, first_pizza - last_employee)
        pizzas_made += last_employee

if not pizzas:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    if employees:
        print(f'Employees: {", ".join(str(x) for x in employees)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizzas)}')
    print(f'')