class Cell():
	def __init__(self, x, y, serialNum):
		self.rackID = x + 10
		self.powerLevel = self.rackID*y
		self.powerLevel += serialNum
		self.powerLevel *= self.rackID
		temp = str(self.powerLevel)
		if len(temp) > 2:
			self.powerLevel = int(temp[len(temp)-3])
		self.powerLevel -= 5

serialNum = int(input("Serial Number? ")) #7139
grid = []
for y in range(302):
	grid.append([])
	for x in range(302):
		grid[y].append(Cell(x, y, serialNum))

maxValue = 0
maxIndex = 0,0
maxSize = 3
values = []
indices = []
for size in range(3,301):
	print (size)
	for y in range(1, 302-size):
		for x in range(1, 302-size):
			subTotal = 0
			for i in range(size):
				for j in range(size):
					subTotal += grid[y+i][x+j].powerLevel
			if subTotal > maxValue:
				maxValue = subTotal
				maxIndex = x,y
				maxSize = size
			values.append(subTotal)
			indices.append((x,y))

'''
for y in range(1,301):
	for x in range(1,301):
		if grid[y][x].powerLevel > -1:
			[print (" ", end='')]
		print (grid[y][x].powerLevel, end=' ')
	print ()
'''
print (maxIndex,end=",")
print (maxSize)