def shop_from_grocery_list(budget, list, *args):
    for product, price in args:
        if product in list and budget - price >= 0:
            budget -= price
            list.remove(product)
        elif product in list and budget - price < 0:
            break
    output = []
    if not list:
        output.append(f'Shopping is successful. Remaining budget: {budget:.2f}.')
    else:
        output.append(f'You did not buy all the products. Missing products: {", ".join(list)}.')
    return "\n".join(output)


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

