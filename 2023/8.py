from itertools import cycle
from math import lcm
from re import search


[instrucs, maps] = open('8.txt').read().strip().split("\n\n")


d = {"L": {}, "R": {}}
for mp in maps.splitlines():
    if m := search(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', mp):
        c, l, r = m.groups()
        d["L"][c] = l
        d["R"][c] = r

i, curr = 0, "AAA"
for dir in cycle(instrucs):
    if curr == "ZZZ": break
    curr = d[dir][curr]
    i += 1

print (i)


# Yields the lengths of all cycles that start at ..A
def cycleFinder():
    # Go to next region
    def inc(curr, i):
        return d[instrucs[i]][curr], (i + 1) % len(instrucs)

    for curr in [x for x in d["L"] if x[-1] == "A"]:
        # Find where the cycle starts
        i, seen = 0, set()
        while (curr, i) not in seen:
            seen.add((curr, i))
            curr, i = inc(curr, i)
        cycleStart = (curr, i)

        # Find the cycle's length
        curr, i = inc(curr, i)
        length = 1
        while (curr, i) != cycleStart:
            length += 1
            curr, i = inc(curr, i)
        yield length


# This is a bit of a hack that only works for the input. Turns out each cycle
# only has a single ..Z and it's always exactly on the length of the cycle
print (lcm(*cycleFinder()))
