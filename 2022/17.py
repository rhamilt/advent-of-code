jets = open("17.txt").read().strip()

SHAPES = ["hor", "cross", "l", "ver", "sq"]

def shape_positions(shape, height):
    if shape == "hor":
        pos = [(3, height + 4),(4, height + 4),(5, height + 4),(6, height + 4)]
    elif shape == "cross":
        pos = [(4, height + 4),(4, height + 5),(4, height + 6),(5, height + 5), (3, height + 5)]
    elif shape == "l":
        pos = [(4, height + 4),(3, height + 4),(5, height + 4),(5, height + 5), (5, height + 6)]
    elif shape == "ver":
        pos = [(3, height + 4),(3, height + 5),(3, height + 6),(3, height + 7)]
    else:
        pos = [(3, height + 4),(4, height + 4),(3, height + 5),(4, height + 5)]
    return pos


rocks = {(i, 0) for i in range(1, 8)}
shape = 0
c = 0
i = 1
while True:
    shape_pos = shape_positions(SHAPES[shape], max(rocks, key=lambda x: x[1])[1])
    shape = (shape + 1) % len(SHAPES)
    while True:
        if jets[c] == ">":
            if all((pos[0] + 1, pos[1]) not in rocks and pos[0] < 7 for pos in shape_pos):
                shape_pos = list(map(lambda x: (x[0] + 1, x[1]), shape_pos))
        else:
            if all((pos[0] - 1, pos[1]) not in rocks and pos[0] > 1 for pos in shape_pos):
                shape_pos = list(map(lambda x: (x[0] - 1, x[1]), shape_pos))
        c = (c + 1) % len(jets)
        if all((pos[0], pos[1] - 1) not in rocks for pos in shape_pos):
            shape_pos = list(map(lambda x: (x[0], x[1] - 1), shape_pos))
        else: break

    rocks = rocks.union(set(shape_pos))

    if i == 2022: print (max(rocks, key=lambda x: x[1])[1])

    i += 1
