from collections import defaultdict

NUMS = "0123456789"

grid = open("3.txt").read().strip().split("\n")


def in_range(r, c):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])


def adj(r, c):
    valid = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if in_range(r + i, c + j):
                valid |= grid[r + i][c + j] != "." and grid[r + i][c + j] not in NUMS
    return valid


def adj_gears(r, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if in_range(r + i, c + j):
                if grid[r + i][c + j] == "*": return (r + i, c + j)

    return (-1, -1)


tot = 0
gears = defaultdict(list)
for r in range(len(grid)):
    c = 0
    while c < len(grid[r]):
        if grid[r][c] in NUMS:
            cs = []
            while c < len(grid[r]) and grid[r][c] in NUMS:
                cs.append(c)
                c += 1
            if any(adj(r, c_) for c_ in cs):
                tot += int(grid[r][cs[0]:c])
            for c_ in cs:
                gr, gc = adj_gears(r, c_)
                if gr != -1:
                    gears[(gr, gc)].append(int(grid[r][cs[0]:c]))
                    break
        else:
            c += 1

# Only take gears with two adjacents
gears = {k: v for k, v in gears.items() if len(v) == 2}

print (tot) # Part 1
print (sum(a[0] * a[1] for a in gears.values())) # Part 2
