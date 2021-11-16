def coordToIndex(row, col, cols):
	return row*cols + col

def indexToCoord(ind, cols):
	return (ind//cols, ind%cols)

def manhattanCalculator(row, col, coords):
	distances = {}
	for key, coord in coords.items():
		x = coord[0]
		y = coord[1]
		distances[key] = abs(row-x) + abs(col-y)
	return distances

def display(grid, rows, cols):
	for row in range(rows):
		for col in range(cols):
			print (grid[coordToIndex(row, col, cols)], end = '')
		print()

def calcMaxFreqs(grid):
	q_table = {}
	for char in grid:
		if char not in q_table:
			q_table[char] = 0
		q_table[char] += 1
	print (q_table)
	return sorted(q_table, key=q_table.get, reverse=True)

def checkDistances(distances):
	total = 0
	for distance in distances.values():
		total += distance
	if total > 10000:
		return False
	return True

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("6.txt", 'r') as infile:
	lines = infile.readlines()
	coords = {}
	for count, line in enumerate(lines):
		coords[alpha[count]] = (int(line[:line.index(',')]), int(line[line.index(" ")+1:]))

print (coords)
rows = 0
cols = 0
for coord in coords.values():
	if coord[0] > rows:
		rows = coord[0]
	if coord[1] > cols:
		cols = coord[1]

grid = ''
for i in range(rows*cols):
	grid += '.'
for i in range(len(coords)):
	ind = coordToIndex(coords[alpha[i]][0], coords[alpha[i]][1], cols)
	grid = grid[:ind] + str(alpha[i]) + grid[ind+1:]

for i in range(len(grid)):
	if grid[i] == ".":
		row, col = indexToCoord(i, cols)
		distances = manhattanCalculator(row, col, coords)
		keys = sorted(distances, key=distances.get)
		if distances[keys[0]] < distances[keys[1]]:
			grid = grid[:i] + keys[0] + grid[i+1:]
	else:
		grid = grid[:i] + ' ' + grid[i+1:]
#Part 2
for i in range(len(grid)):
	row, col = indexToCoord(i, cols)
	if checkDistances(manhattanCalculator(row, col, coords)):
		grid = grid[:i] + '#' + grid[i + 1:]
display(grid, rows, cols)
print (grid.count('#'))

