def shopping_cart(*args):
    meals = {'Soup': [], 'Pizza': [], 'Dessert': []}
    limits = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}

    for info in args:
        if info == 'Stop':
            break
        meal, product = info
        if meal in meals and len(meals[meal]) < limits[meal] and product not in meals[meal]:
            meals[meal].append(product)

    if all(len(x) == 0 for x in meals.values()):
        return f'No products in the cart!'

    output = []
    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    for meal, products in sorted_meals:
        output.append(f'{meal}:')
        [output.append(f' - {product}') for product in sorted(products)]

    return "\n".join(output)


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

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

