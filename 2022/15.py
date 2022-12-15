from re import findall

lines = open("15.txt").read().strip().split("\n")

def m(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

dists = {}
beacons = set()
for line in lines:
    s1, s2, b1, b2 = list(map(int, findall(r'-?\d+', line)))
    dists[(s1, s2)] = m(s1, s2, b1, b2)
    beacons.add((b1, b2))

invalid = set()
y_col = 2000000
# Go through each sensor and find all the points in the y_col that are in range of that sensor.
# Once we add that all up and get rid of the beacons in that row, that is our result
for (x, y), dist in dists.items():
    if abs(y_col - y) < dist:
        min_x = x - (dist - abs(y_col - y))
        max_x = x + (dist - abs(y_col - y)) + 1
        invalid = invalid.union(set(range(min_x, max_x)))

# Part 1: Went alright, moved quickly but got hung up on a few things. Not particularly quick
print (len(invalid) - len(set([b for b in beacons if b[1] == y_col])))

# p_lines is all the lines that have form y = x + b
p_lines = set()
# n_lines is all the lines that have form y = -x + b
n_lines = set()
# Add all the different possible lines (represented by their y intercepts)
for (x, y), dist in dists.items():
    p_lines.add(y - x + dist + 1)
    n_lines.add(y - x + dist + 1)
    p_lines.add(y + x - dist - 1)
    n_lines.add(y + x - dist - 1)

# Find all the intersections of the differently sloped line segments.
# The the intersection of two lines y = x + a and y = -x + b is ((b - a) / 2, (b + a) / 2)
intersections = set(((n - p) // 2 , (n + p) // 2) for n in n_lines for p in p_lines)
boundary = 4000000
# Go through each intersection. If it can't be found by any of the sensors, we know we have the
# right one
for i in intersections:
    if 0 < i[0] < boundary and 0 < i[1] < boundary:
        if all(m(*i, *sensor) > dists[sensor] for sensor in dists):
            # Part 2: Spent a really long time thinking about this, but the bonus here is that it
            # is really fast and really well thought out
            print (boundary * i[0] + i[1])
            break