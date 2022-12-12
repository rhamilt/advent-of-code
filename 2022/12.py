def get_adj(grid, r, c):
    adj = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if abs(i) != abs(j):
                if r + i in range(len(grid)) and c + j in range(len(grid[r])):
                    if grid[r][c] - grid[r+i][c+j] <= 1:
                        adj.append((r + i, c + j))
    return adj

lines = open("12.txt").read().strip().split("\n")
grid = [list(map(ord, line)) for line in lines]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == ord('S'):
            grid[row][col] = ord('a')
            s = (row, col)
        if grid[row][col] == ord('E'):
            grid[row][col] = ord('z')
            e = (row, col)

dists = {}
frontier = {e: 0}
a = float('inf')
while s not in dists:
    min_dist_key = (r, c) = min(frontier, key=lambda x: frontier[x])
    min_dist = frontier.pop(min_dist_key)

    # Added for part 2
    # If the character is a, we say that the distance between the closest a to the destination is
    # the minimum of the current distance from the destination or whatever a already is
    if grid[r][c] == ord('a'): a = min(a, min_dist)

    dists[min_dist_key] = min_dist
    for adj in get_adj(grid, r, c):
        if adj not in dists:
            frontier[adj] = min_dist + 1

# Part 1: I really showed how much of a fool I am. I kind of stumbled through this puzzle, ending
# up with a semi-djikstra. What really let me down was the fact that I thought that we could only
# go up or down a single level of elevation, but it can actually go down any number
print (dists[s])
# Part 2: This was actually really easy because I did it backwards, so I just print whatever 'a' I
# found first. Did it in about a minute
print (a)