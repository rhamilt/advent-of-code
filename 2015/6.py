import re

def read(instruc):
	s = re.search(r'(.*) (\d*),(\d*) \w* (\d*),(\d*)', instruc)
	type = s.group(1)
	sr, sc = int(s.group(2)), int(s.group(3)) #start row/col
	er, ec = int(s.group(4)), int(s.group(5)) #end row/col
	if type == "turn on": return (1, sr, sc, er, ec)
	elif type == "turn off": return (0, sr, sc, er, ec)
	else: return (-1, sr, sc, er, ec)

instrucs = list(map(str.strip, open('6.txt', 'r').readlines()))
grid = [[0 for c in range(1000)] for r in range(1000)]

for upinstruct in instrucs: #up is unparsed
	instruc = read(upinstruct)
	for r in range(instruc[1], instruc[3]+1):
		for c in range(instruc[2], instruc[4]+1):
			grid[r][c] = instruc[0] if instruc[0] == 0 or instruc[0] == 1 else 1-grid[r][c]
print (sum([sum(grid[r]) for r in range(1000)])) #part 1: nothing special to report here

grid = [[0 for c in range(1000)] for r in range(1000)]

for upinstruct in instrucs: #up is unparsed
	instruc = read(upinstruct)
	for r in range(instruc[1], instruc[3]+1):
		for c in range(instruc[2], instruc[4]+1):
			if instruc[0] == 1: grid[r][c] += 1
			elif instruc[0] == 0: grid[r][c] -= 1
			else: grid[r][c] += 2
			if grid[r][c] < 0: grid[r][c] = 0

print (sum([sum(grid[r]) for r in range(1000)])) #part 1: nothing special to report here