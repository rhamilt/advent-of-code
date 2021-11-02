from re import search

def grid_p(grid):
	for row in grid:
		print (''.join(map(str,row)).replace('1','x').replace('0','.'))
	print ()

lines = open('8.txt', 'r').read().split('\n')
grid = [[0 for c in range(50)] for r in range(6)]

for line in lines:
	if 'rect' in line:
		s = search(r'(\d+)x(\d+)', line).groups()
		col, row = int(s[0]), int(s[1])
		for r in range(len(grid)):
			for c in range(len(grid[0])):
				if r < row and c < col: grid[r][c] = 1
	elif 'row' in line:
		s = search(r'=(\d+) by (\d+)', line).groups()
		row, size = int(s[0]), int(s[1])
		temp = [[grid[r][c] for c in range(len(grid[0]))] for r in range(len(grid))] #makes deep copy of grid
		for i in range(len(temp[0])-1, -1, -1):
			temp[row][i] = grid[row][i-size]
		grid = temp
	else:
		s = search(r'=(\d+) by (\d+)', line).groups()
		col, size = int(s[0]), int(s[1])
		temp = [[grid[r][c] for c in range(len(grid[0]))] for r in range(len(grid))] #makes deep copy of grid
		for i in range(len(temp)-1, -1, -1):
			temp[i][col] = grid[i-size][col]
		grid = temp


print (sum(sum(row) for row in grid)) #part 1: my idea was rock solid the whole time, but as one might expect I made copy error
grid_p(grid) #part 2: firts try, didn't understand question at first, but i like clever puzzle design and i'd already made grid_p