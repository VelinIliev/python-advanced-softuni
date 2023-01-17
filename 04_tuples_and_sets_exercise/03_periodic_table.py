chemical_elements = set()
for line in range(int(input())):
    [chemical_elements.add(element) for element in input().split()]

print(*chemical_elements, sep="\n")
