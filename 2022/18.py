lines = open("18.txt").read().strip().split("\n")
droplets = [tuple(map(int, line.split(','))) for line in lines]

MAX_X = max(droplets, key=lambda x: x[0])[0]
MAX_Y = max(droplets, key=lambda x: x[1])[1]
MAX_Z = max(droplets, key=lambda x: x[2])[2]

# Cubes are adjacent if exactly 1 of the components has a difference of 1, while the others have a
# difference of zero
def adj(x1, y1, z1, x2, y2, z2):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1

# Returns all the adjacents that are not in seen and are adjacent as defined by the above function
def adjacents(x, y, z, seen):
    adjacents = set()
    for i in range(-1, 2):
        if x + i not in range(0, MAX_X + 1): continue
        for j in range(-1, 2):
            if y + j not in range(0, MAX_Y + 1): continue
            for k in range(-1, 2):
                if z + k not in range(0, MAX_Z + 1): continue
                if not adj(x, y, z, x + i, y + j, z + k): continue
                p = (x + i, y + j, z + k)
                if p not in seen and p not in droplets:
                    adjacents.add(p)

    return adjacents

# To calculate the area, we find the total area of all cubes and then subtract two every time two
# cubes are adjacent.
def area(cubes):
    area = len(cubes) * 6
    for i1 in range(len(cubes)):
        d1 = cubes[i1]
        for i2 in range(i1 + 1, len(cubes)):
            d2 = cubes[i2]
            if adj(*d1, *d2): area -= 2
    return area

droplet_area = area(droplets)
# Part 1: Pretty easy, fooled around too much and got the wrong definition of adjacent (why hath
# God cursed me with stupidity)
print (droplet_area)

# Calculate all the cubes of air that we can reach in the region
frontier = [(0, 0, 0)]
seen = {(0, 0, 0)}
while frontier:
    point = frontier.pop()
    adjacent_points = adjacents(*point, seen)
    seen = seen.union(adjacent_points)
    frontier += list(adjacent_points)

all_cubes = {(x, y, z) for x in range(MAX_X) for y in range(MAX_Y) for z in range(MAX_Z)}
# The bubble area is the surface area of the air that we havent seen (ie. trapped in the lava).
# The air that we havent seen is the difference between all the air and the air we have seen
# + the droplets of lava.
bubble_area = area(list(all_cubes.difference(seen.union(set(droplets)))))
# Part 2: I originally thought too much about the example, and concluded that all trapped air
# pockets were a single cube with surface area 6. How stupid of me.
print (droplet_area - bubble_area)