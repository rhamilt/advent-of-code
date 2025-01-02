from collections import defaultdict
from itertools import combinations

G = open('8.txt').read().split()
g = {(r, c): G[r][c] for r in range(len(G)) for c in range(len(G[r]))}
nodes = defaultdict(list)
for k, v in filter(lambda x: x[1] != ".", g.items()):
    nodes[v].append(k)

def dv(r1, c1, r2, c2):
    return (r1 - r2), (c1 - c2)

def add(r, c, dr, dc, n=1, sub=False):
    if sub:
        return r - n * dr, c - n * dc
    else:
        return r + n * dr, c + n * dc

antis1 = set()
antis2 = set()
for coords in nodes.values():
    for a, b in combinations(coords, 2):
        diff = dv(*a, *b)
        n = 0
        while add(*a, *diff, n) in g:
            antis2.add(add(*a, *diff, n))
            if n == 1: antis1.add(add(*a, *diff, n))
            n += 1
        n = 0
        while add(*b, *diff, n, sub=True) in g:
            antis2.add(add(*b, *diff, n, sub=True))
            if n == 1: antis1.add(add(*b, *diff, n, sub=True))
            n += 1

print (len(antis1))
print (len(antis2))
