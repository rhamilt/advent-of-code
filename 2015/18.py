def neighbor_count(grid, r, c):
	count = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if grid[r+i][c+j] == '#':
				if i != 0 or j != 0:
					count += 1 
	return count # could have gone one line but this was faster?

def copy(grid):
	return [[grid[r][c] for c in range(102)] for r in range(102)]

grid = [['.' for i in range(102)]]
for line in map(str.strip, open('18.txt', 'r')):
	grid.append(list('.'+line+'.'))
grid.append(['.' for i in range(102)])

grid[1][1] = '#' #comment out for part 1
grid[1][100] = '#'
grid[100][1] = '#'
grid[100][100] = '#'

for iteration in range(100):
	temp_grid = copy(grid)
	for r in range(1, 101):
		for c in range(1, 101):
			n_count = neighbor_count(grid, r, c)
			if (r, c) == (1, 1) or (r, c) == (1, 100) or (r, c) == (100, 1) or (r, c) == (100, 100):
				temp_grid[r][c] = '#'
			elif grid[r][c] == '#':
				if n_count != 2 and n_count != 3: temp_grid[r][c] = '.'
			else:
				if n_count == 3: temp_grid[r][c] = '#'
	grid = copy(temp_grid)

print (sum([1 for r in range(102) for c in range(102) if grid[r][c] == '#'])) #part 1: relatively simple, made errors in neighbor count calculation (counted self)
