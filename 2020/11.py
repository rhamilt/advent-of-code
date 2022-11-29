lines = open("11.txt").read().split("\n")
grid = [[*line] for line in lines]

# Count the number of adjacent seats that are full
def count_adj(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if r + i >= 0 and r + i < len(grid) and c + j >= 0 and c + j < len(grid[0]):
                    if grid[r + i][c + j] == "#": count += 1
    return count

# Count the number of visible seats that are full. A seat is visible from a given seat if there is
# only floor between them
def count_vis(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                k, l = 1, 1
                while r + i * k >= 0 and r + i * k < len(grid) and c + j * l >= 0 and c + j * l < len(grid[0]):
                    if grid[r + i * k][c + j * l] == "#": count += 1; break
                    elif grid[r + i * k][c + j * l] == "L": break
                    k += 1; l += 1
    return count

def run(grid, count_func, adjacent_full_limit):
    while True:
        temp_grid = [[c for c in row] for row in grid]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "L":
                    adj_count = count_func(grid, r, c)
                    temp_grid[r][c] = "#" if adj_count == 0 else "L"
                elif grid[r][c] == "#":
                    adj_count = count_func(grid, r, c)
                    temp_grid[r][c] = "#" if adj_count < adjacent_full_limit else "L"
                else: temp_grid[r][c] = "."
        if temp_grid == grid: break
        grid = [[c for c in row] for row in temp_grid]
    print (sum(row.count("#") for row in grid))

# Part 1: ran in to issues with array copying as I always do. Accidentally reversed > with < as
run(grid, count_adj, 4)
# Part 2: took a couple of tries to get right, but it's actually pretty easy to just add count_vis
run(grid, count_vis, 5)
