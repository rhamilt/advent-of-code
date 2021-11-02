DIREC = {'U' : (0,1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)} #In cartesian coordinates

def get_points(direcs):
	grid = {}
	x = 0
	y = 0
	count = 0
	for direction in direcs:
		direc, num = direction[0], int(direction[1:])
		for i in range(num):
			x += DIREC[direc][0]
			y += DIREC[direc][1]
			count += 1
			if (x, y) not in grid:
				grid[(x,y)] = count
	return grid

with open('day3.txt', 'r') as infile:
	direc1 = infile.readline().strip().split(',')
	direc2 = infile.readline().strip().split(',')


grid1 = get_points(direc1)
grid2 = get_points(direc2)

matches = set(grid1.keys()).intersection(set(grid2.keys()))
print (matches)

#PART 1: Originally tried to use dictionary where item was number of wires crossing a given point, but it just didn't work.
print(min([abs(loc[0])+abs(loc[1]) for loc in matches]))
#Part 2
print(min([grid1[loc]+grid2[loc] for loc in matches]))