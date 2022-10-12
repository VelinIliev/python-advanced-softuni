eggs_sizes = [int(x) for x in input().split(", ")]
paper_sizes = [int(x) for x in input().split(", ")]

box_size = 50
boxes = 0

while eggs_sizes and paper_sizes:
    egg = eggs_sizes[0]
    paper = paper_sizes[-1]
    if egg <= 0:
        eggs_sizes.pop(0)
        continue
    if egg == 13:
        eggs_sizes.pop(0)
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue

    if egg + paper <= box_size:
        boxes += 1
    eggs_sizes.pop(0)
    paper_sizes.pop()

if boxes > 0:
    print(f'Great! You filled {boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if len(eggs_sizes) > 0:
    print(f'Eggs left: {", ".join(str(x) for x in eggs_sizes)}')
if len(paper_sizes) > 0:
    print(f'Pieces of paper left: {", ".join(str(x) for x in paper_sizes)}')