lines = int(input())

chemical_elements = set( )
for line in range(lines):
    elements = input().split()
    for element in elements:
        chemical_elements.add(element)

[print(element) for element in chemical_elements]