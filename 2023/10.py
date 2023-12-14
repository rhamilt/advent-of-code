from collections import deque


DIRECTIONS = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}

TYPES = {
    (-1, 0): {"7", "F", "|"},
    (1, 0): {"L", "J", "|"},
    (0, -1): {"-", "F", "L"},
    (0, 1): {"-", "7", "J"},
}


grid = open("10.txt").readlines()


dists = {}
q = deque()

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "S":
            q.append(((r, c), 0))

# BFS
while len(q):
    curr, dist = q.popleft()
    if curr in dists and dists[curr] < dist: continue
    dists[curr] = dist

    r, c = curr
    for i, j in DIRECTIONS[grid[r][c]]:
        if r + i >= 0 and r + i < len(grid) and c + j >= 0 and c + j < len(grid[r]):
            if grid[r + i][c + j] in TYPES[(i, j)]:
                q.append(((r + i, c + j), dist + 1))

print (max(dists.values()))

# Nifty parity solution
# Realized that you could see if you're inside the loop based on how many times
# you've crossed a vertical bar. Depending on how you view parity, you can use
# either, |F7 as pipes or |LJ as pipes, but not mixing them
inner_region_size = 0
for r in range(len(grid)):
    inside = False
    for c in range(len(grid[r])):
        if (r, c) in dists and grid[r][c] in '|F7':
            inside = not inside
        else:
            inner_region_size += inside and (r, c) not in dists

print (inner_region_size)
