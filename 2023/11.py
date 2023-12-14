def man(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

def extras(a, b, xtras):
    return sum(1 for x in xtras if a < x < b or b < x < a)


grid = open('11.txt').readlines()

empty_rows = set(i for i, r in enumerate(grid) if "#" not in r)
empty_cols = set(c for c in range(len(grid[0])) if not any(r[c] == "#" for r in grid))

galaxies = {(r, c): {} for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "#"}
for g1 in galaxies:
    for g2 in galaxies:
        if g1 != g2:
            galaxies[g1][g2] = man(g1, g2) + extras(g1[0], g2[0], empty_rows) + extras(g1[1], g2[1], empty_cols)

print (sum(map(lambda x: sum(x.values()), galaxies.values())) // 2)

for g1 in galaxies:
    for g2 in galaxies:
        if g1 != g2:
            galaxies[g1][g2] = man(g1, g2) + (10**6 - 1) * (extras(g1[0], g2[0], empty_rows) + extras(g1[1], g2[1], empty_cols))

print (sum(map(lambda x: sum(x.values()), galaxies.values())) // 2)
