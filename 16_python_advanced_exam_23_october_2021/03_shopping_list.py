def shopping_list(budget, **kwargs):
    budget = budget
    return_string = ""
    products = []
    if budget < 100:
        return f'You do not have enough budget.'
    for product, data in kwargs.items():
        if len(set(products)) > 4:
            break
        price = data[0]
        quantity = data[1]
        total_price = price * quantity
        if total_price <= budget:
            return_string += f'You bought {product} for {total_price:.2f} leva.\n'
            budget -= total_price
            products.append(product)
    return return_string



print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
