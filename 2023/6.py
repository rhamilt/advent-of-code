from functools import reduce

# This code is not very readable, i just wanted to write something compact
def beats_max(a, v):
    t, d = v
    return a * len([p for p in [i * (t - i) for i in range(t)] if p > d])


times, distances = map(lambda x: list(map(int, x.split()[1:])), open("6.txt").readlines())
print (reduce(beats_max, zip(times, distances), 1))

time = int(''.join(map(str, times)))
distance = int(''.join(map(str, distances)))

# Part 2 kind of slow but it works, finds the lower and upper bound of range
# There's some quadratic math to figure out the exact endpoints, this doesn't
# take that long anyway
i = 0
while i * (time - i) < distance:
    i += 1

j = i
while i * (time - i) > distance:
    i += 1

print (i - j)
