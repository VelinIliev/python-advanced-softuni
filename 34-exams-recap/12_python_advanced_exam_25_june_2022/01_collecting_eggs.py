egg_size = [int(x) for x in input().split(", ")]
paper_size = [int(x) for x in input().split(", ")]

box_size = 50
filled_boxes = 0

while egg_size and paper_size:
    egg = egg_size.pop(0)

    if egg <= 0:
        continue

    if egg == 13:
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue

    paper = paper_size.pop()

    if paper + egg <= box_size:
        filled_boxes += 1

if filled_boxes > 0:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if egg_size:
    print(f'Eggs left: {", ".join(str(x) for x in egg_size)}')
if paper_size:
    print(f'Pieces of paper left: {", ".join(str(x) for x in paper_size)}')