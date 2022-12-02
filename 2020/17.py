lines = open("17.txt").read().strip().split("\n")

# Get a set of all coordinates that are adjacent to the given point
def getAdjacents(coord, dimensions):
    (x, y, z, w) = coord

    # We only want to vary the fourth dimensions if we actually have 4 dimensions
    fourth_dim_range = range(-1, 2) if dimensions == 4 else range(0, 1)

    coords = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in fourth_dim_range:
                    if not (i == 0 and j == 0 and k == 0 and l == 0):
                        coords.add((x + i, y + j, z + k, w + l))
    return coords

# Returns the number of adjacent points that are on
def num_adjacent_on(space, adjacents):
    return (sum(1 for adjacent in adjacents if adjacent in space))

# Runs the conway simulation in the given number of dimensions for `n` steps
def conway(n, dimensions):
    space = set()
    # Add our starting points to the space
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == "#":
                space.add((x, y, 0, 0))

    for _ in range(n):
        temp_space = set()
        seen = set()
        # Basically a deepcopy
        frontier = space.union(set())
        while len(frontier) > 0:
            point = frontier.pop()
            if point not in seen:
                adjacents = getAdjacents(point, dimensions)
                adjacents_on = num_adjacent_on(space, adjacents)

                if point in space:
                    if adjacents_on == 2 or adjacents_on == 3:
                        temp_space.add(point)
                    # Only add the adjacents to the frontier if the current point is on -- we don't
                    # want to add ones that are adjacent to off
                    frontier = frontier.union(adjacents.difference(seen))
                else:
                    if adjacents_on == 3:
                        temp_space.add(point)
                seen.add(point)

        # Another deepcopy
        space = temp_space.union(set())
    return len(space)

print (conway(6, 3))
print (conway(6, 4))