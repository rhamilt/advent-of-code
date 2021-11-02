class Rectangle():
	def __init__(self, num, x, y, rows, cols):
		self.number = num
		self.x = x
		self.y = y
		self.rows = rows
		self.cols = cols
with open('3.txt', 'r') as infile:
	lines = []
	for line in infile:
		lines.append(line)
#Part 1
rectangles = []
for line in lines:
	if line != '':
		rectangles.append(Rectangle(line[1:line.index(" ")], int(line[line.index('@')+2:line.index(",")]), int(line[line.index(",")+1:line.index(":")]), \
		int(line[line.index(":") + 2: line.index("x")]), int(line[line.index('x') + 1:len(line)-1])))
filled_indices = {}
for rectangle in rectangles:
	for r in range(rectangle.x, rectangle.x + rectangle.rows):
		for c in range(rectangle.y, rectangle.y + rectangle.cols):
			if (r,c) not in filled_indices:
				filled_indices[(r,c)] = 0
			filled_indices[(r,c)] += 1
count = 0
for ind in filled_indices:
	if filled_indices[ind] > 1:
		count += 1
print (count)
#Part 2
for rectangle in rectangles:
	unoverlapped = True
	for r in range(rectangle.x, rectangle.x + rectangle.rows):
		for c in range(rectangle.y, rectangle.y + rectangle.cols):
			if filled_indices[r,c] != 1:
				unoverlapped = False
	if unoverlapped:
		print (rectangle.number)