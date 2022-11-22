grid = list(map(str.strip, open("3.txt").readlines()))

r, c, count = 0, 0, 0
while r < len(grid):
    if grid[r][c] == "#": count += 1
    c = (c + 3) % len(grid[0])
    r += 1

# part 1: No issues
print (count)

product = 1
for i in [1, 3, 5, 7]:
    r, c, count = 0, 0, 0
    while r < len(grid):
        if grid[r][c] == "#": count += 1
        c = (c + i) % len(grid[0])
        r += 1
    product *= count

r, c, count = 0, 0, 0
while r < len(grid):
    if grid[r][c] == "#": count += 1
    r = r + 2
    c = (c + 1) % len(grid[0])
product *= count

# part 2: Initially did not realize that there is one that goes down by two, which slowed me down
print (product)
