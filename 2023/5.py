lines = open("5.txt").read().strip().split("\n\n")

seeds_str, map_strs = lines[0], lines[1:]

vals = list(map(int, seeds_str.split(": ")[1].split()))
rules = [list(map(str.split, map_strs[i].split("\n")[1:])) for i in range(len(map_strs))]
seed_ranges = sorted(zip(vals[::2], vals[1::2]))

def in_seed_range(seed):
    return any(seed > rng[0] and seed < rng[0] + rng[1] for rng in seed_ranges)

def location(val):
    for rule in rules:
        mp = [tuple(map(int, rng)) for rng in rule]
        for dst, src, rng in mp:
            if val > src and val < src + rng:
                val = dst + (val - src)
                break
    return val


def seed_from_location(val):
    for rule in reversed(rules):
        mp = [tuple(map(int, rng)) for rng in rule]
        for src, dst, rng in mp:
            if val > src and val < src + rng:
                val = dst + (val - src)
                break
    return val

print (min(location(val) for val in vals))

# BRUTE FORCE LOL
loc = 0
while not in_seed_range(seed_from_location(loc)): loc += 1
print (loc)
