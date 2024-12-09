from collections import defaultdict

lines = open("4.txt").readlines()
grid = defaultdict(str, {(r, c): lines[r][c] for r in range(len(lines)) for c in range(len(lines[0]))})

keys = list(grid.keys())
d = -1, 0, 1

print (sum("".join([grid[(r + i * n, c + j * n)] for n in range(4)]) == "XMAS" for r, c in keys for i in d for j in d))

massam = "MAS", "SAM"
print (sum("".join([grid[(r + i, c + i)] for i in d]) in massam and "".join([grid[(r + i, c - i)] for i in d]) in massam for r, c in keys))
