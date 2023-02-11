def shopping_cart(*args):
    meals = {'Soup': [], 'Pizza': [], 'Dessert': []}
    max_meals = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}

    for command in args:
        if command == 'Stop':
            break
        meal, product = command
        if meal in meals and len(meals[meal]) < max_meals[meal]:
            if product not in meals[meal]:
                meals[meal].append(product)

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

    return_list = []
    if all(len(value) == 0 for value in meals.values()):
        return 'No products in the cart!'
    for meal, products in sorted_meals:
        return_list.append(f'{meal}:')
        [return_list.append(f' - {pr}') for pr in sorted(products)]
    return '\n'.join(return_list)


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
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
