def forecast(*args):
    conditions = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }
    for location, weather in args:
        if weather in conditions:
            conditions[weather].append(location)

    return_list = []
    for condition, locations in conditions.items():
        for location in sorted(locations):
            return_list.append(f'{location} - {condition}')
    return '\n'.join(return_list)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))
#
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
