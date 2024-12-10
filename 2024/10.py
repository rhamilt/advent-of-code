from collections import defaultdict, deque

g = [[int(x) for x in s] for s in open("10.txt").read().splitlines()]
M = defaultdict(int, {(r, c): g[r][c] for r in range(len(g)) for c in range(len(g[r]))})
m = list(M.items())

def walk(coord):
    trails = deque([coord])
    while trails and not M[trails[0]] == 9:
        tr, tc = trails.popleft()
        for i in -1,0,1:
            for j in -1,0,1:
                if abs(i) + abs(j) == 1 and M[tr + i, tc + j] == M[tr, tc] + 1:
                    trails.append((tr + i, tc + j))
    return trails

print (sum(len(set(walk(c))) for c, v in m if not v))
print (sum(len(walk(c)) for c, v in m if not v))
