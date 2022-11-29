import math

lines = open("12.txt").read().split("\n")

loc = [0, 0]
direc = 0
for line in lines:
    instruc, val = line[0], int(line[1:])
    if instruc == "N":
        loc[1] += val
    elif instruc == "S":
        loc[1] -= val
    elif instruc == "E":
        loc[0] += val
    elif instruc == "W":
        loc[0] -= val
    elif instruc == "L":
        direc = (direc + val) % 360
    elif instruc == "R":
        direc = (direc - val) % 360
    elif instruc == "F":
        if direc == 0:
            loc[0] += val
        elif direc == 90:
            loc[1] += val
        elif direc == 180:
            loc[0] -= val
        elif direc == 270:
            loc[1] -= val

# part 1: easy money
print (sum(map(abs, loc)))

loc = [0, 0]
point = [10, 1]
for line in lines:
    instruc, val = line[0], int(line[1:])
    print (line)
    if instruc == "N":
        point[1] += val
    elif instruc == "S":
        point[1] -= val
    elif instruc == "E":
        point[0] += val
    elif instruc == "W":
        point[0] -= val
    elif instruc == "L":
        val = val * math.pi / 180
        point = [(int(math.cos(val)) * (point[0]) - int(math.sin(val)) * (point[1])),
                 (int(math.sin(val)) * (point[0]) + int(math.cos(val)) * (point[1]))]
    elif instruc == "R":
        if val == 180:
            point = [-1 * point[0], -1 * point[1]]
        else:
            val = val * math.pi / 180
            point = [-1 * (int(math.cos(val)) * (point[0]) - int(math.sin(val)) * (point[1])),
                    -1 * (int(math.sin(val)) * (point[0]) + int(math.cos(val)) * (point[1]))]
    elif instruc == "F":
        loc[0] += point[0] * val
        loc[1] += point[1] * val

# part 1: Took a long time to realize that R180 was giving me the wrong result. ended up not
# doing any rotation at all, instead of a true -180
print (sum(map(abs, loc)))