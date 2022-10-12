def shopping_cart(*args):
    cart = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    max_meal = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    return_string = ""
    for info in args:
        if info == "Stop":
            break
        else:
            meal = info[0]
            product = info[1]
        if meal in cart and len(cart[meal]) < max_meal[meal]:
            if product not in cart[meal]:
                cart[meal].append(product)
    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
    for meal, products in sorted_cart:
        return_string += f'{meal}:\n'
        sorted_products = sorted(products)
        for product in sorted_products:
            return_string += f' - {product}\n'
    if len(cart["Dessert"]) == 0 and len(cart["Pizza"]) == 0 and len(cart["Soup"]) == 0:
        return_string = f'No products in the cart!'
    return return_string


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))

