def stock_availability(*cakes):
    cupcakes = []
    delivery = False
    sell = False
    for num, cake in enumerate(cakes):
        if type(cake) == list:
            cupcakes = cake
        if cake == "delivery":
            delivery = True
            sell = False
            continue
        if cake == "sell":
            delivery = False
            sell = True
            if num == len(cakes) - 1:
                cupcakes.pop(0)
            continue
        if delivery:
            cupcakes.append(cake)
        if sell:
            if type(cake) == int:
                if cake > len(cupcakes):
                    cupcakes = []
                else:
                    for _ in range(cake):
                        cupcakes.pop(0)
            else:
                if cake in cupcakes:
                    while cake in cupcakes:
                        cupcakes.remove(cake)
    return cupcakes

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print()
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print()
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print()
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print()
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print()
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print()
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))