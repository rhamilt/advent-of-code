import re
from queue import PriorityQueue

lines = open("16.txt").read().strip().split("\n")

valves = {}
lead_to = {}
for line in lines:
    a, b = line.split("; ")
    valve, rate = re.search(r'Valve (\w\w) .*?(\d+)', a).groups()
    valves[valve] = int(rate)
    lead_to[valve] = re.findall(r'[A-Z]{2}', b)

# Djikstra to calculate the distance from all the other valves to `valve`
def dist(valve):
    dists = {valve: 0}
    frontier = PriorityQueue()
    for v in lead_to[valve]:
        frontier.put((1, v))

    while not frontier.empty():
        dist, curr = frontier.get()
        dists[curr] = dist
        for v in lead_to[curr]:
            if v not in dists:
                frontier.put((dist + 1, v))
    return dists

# We only care about non-zero valves
non_empty = {v: r for v, r in valves.items() if r != 0}
dists = {v: dist(v) for v in valves}

def pressure(curr, n, open_valves):
    if n <= 0: return 0, open_valves

    # The pressure that opening the current valve adds is its flow rate multiplied by the current
    # time. The if statement is to account for the "AA" at the start
    curr_pressure = n * non_empty[curr] if curr in non_empty else 0

    sub_pressure = 0
    new_open_valves = open_valves.union({curr})
    # Check out all the valves that have non-zero flow rates
    for v in non_empty:
        # We don't want to go down this recursive path if a) this is the current valve, b) this
        # valve has already been opened, or c) We don't have enough time left to open it
        if curr == v or v in open_valves or dists[curr][v] >= n: continue

        # In our recursive call, we decrease the time by the distance to the next valve + 1 to open
        # it. We also add the current valve to the union of those two
        sp, temp_open_valves = pressure(v, n - dists[curr][v] - 1, open_valves.union({curr}))
        if sp > sub_pressure:
            sub_pressure, new_open_valves = sp, temp_open_valves

    # We return the pressure from this valve combined with the pressure from all the valves we
    # visit after
    return (curr_pressure + sub_pressure, new_open_valves)

# Part 1: Took me a while, but once I settled on removing all the zeros and focusing on the
# distances, this moved pretty quickly. Happy that I figured out a fast and clever solution
me, me_open = pressure("AA", 30, set())
print (me)

me, me_open = pressure("AA", 26, set())
el, el_open = pressure("AA", 26, me_open)
# Part 2: Farted around for a long time working on a solution that tried to have me and the
# elephant going around in parallel. I then thought, they would definitely not be stopping at any
# of the same valves, so I can just have the elephant ignore all the valves that I visit, and find
# the best pressure for the elephant opening all of the other valves. This does not work when there
# is a case that one of us runs out of work to do (ie. the elephant and I can get to all of the
# closed non-zero valves before the time runs out). This means it does not work on the example
print (me + el)
