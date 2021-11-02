import sys
class Goblin():
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.symbol = 'G'
		self.hp = 200
	def hasOpponents(opponents):
		return not (len(opponents) == 0)
class Elf():
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.symbol = 'E'
		self.hp = 200
	def hasOpponents(opponents):
		return not (len(opponents) == 0)

def sortLocations(locations):
	sortedLocations = []
	for location in locations:
		for i in len(sortedLocations):
			if location[0] < sortedLocations[i][0]:
				sortedLocations.insert(i, location)
				break
			if location[0] == sortedLocations[i][0]:
				if locations[1] < sortedLocations[i][1]:
					sortedLocations.insert(i, location)
					break
				else:
					sortedLocations.insert(i+1, location)
					break
	return sortedLocations

def display(cavern):
	for y in range(32):
		for x in range(32):
			print (cavern[y][x], end='')
		print ()

cavern = []
goblins = []
elves = []
with open("day15_input.txt", 'r') as infile:
	for y in range(32):
		cavern.append([])
		line = infile.readline()
		x = 0
		for char in line:
			cavern[y].append(char)
			if char == 'G':
				goblins.append([Goblin(y,x)])
			elif char == 'E':
				elves.append([Elf(y,x)])
			x += 1

display(cavern)
print (sortLocations([(5, 10), (10,5)]))
'''
round = 0
while True:
	for y in range(32):
		for x in range(32):
			for goblin in goblins:
				if goblin.y == y and goblin.x == x:
					if goblin.hasOpponents(elves):

					else:
						totalHP = 0
						for goblin in goblins:
							totalHP += goblin.hp
						print (totalHP*round)
	round += 1
'''












	