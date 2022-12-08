lines = open("8.txt").read().strip().split("\n")

visible = set()
for r in range(len(lines)):
    m1, m2 = -1, -1
    for c in range(len(lines)):
        # Examine the regular grid, left to right
        if int(lines[r][c]) > m1:
            visible.add((r, c))
            m1 = int(lines[r][c])
        # Examine the transposed grid, aka regular grid top to bottom
        if int(lines[c][r]) > m2:
            visible.add((c, r))
            m2 = int(lines[c][r])

    m1, m2 = -1, -1
    for c in range(len(lines) - 1, -1, -1):
        # Examine the regular grid, right to left
        if int(lines[r][c]) > m1:
            visible.add((r, c))
            m1 = int(lines[r][c])
        # Examine the transposed grid, aka regular grid bottom to top
        if int(lines[c][r]) > m2:
            visible.add((c, r))
            m2 = int(lines[c][r])

# Part 1: Evil keeps befalling me. My computer randomly shut off. Then I missed that a tree height
# can be 0, which meant that starting the max height at 0 did not work. Very frustrating
print (len(visible))

def score(grid, r, c):
    height = int(grid[r][c])
    prod = 1

    # looking down
    i = 1
    while r + i < len(grid) - 1 and int(grid[r + i][c]) < height:
        i += 1
    prod *= (i)

    # looking up
    i = 1
    while r - i > 0 and int(grid[r - i][c]) < height:
        i += 1
    prod *= (i)

    # looking right
    i = 1
    while c + i < len(grid) - 1 and int(grid[r][c + i]) < height:
        i += 1
    prod *= (i)

    # looking left
    i = 1
    while c - i > 0 and int(grid[r][c - i]) < height:
        i += 1
    prod *= (i)

    return prod

# Part 2: Wasted a lot of time without realizing that edges can't count
print (max(score(lines, r, c) for r in range(1, len(lines) - 1) for c in range(1, len(lines) - 1)))