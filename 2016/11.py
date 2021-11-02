#TODO: implement heapq



import heapq

GOAL = (set(), set(), set(), {'PrG', 'PrC','CoG', 'CuG', 'RuG', 'PlG', 'CoC', 'CuC', 'RuC', 'PuC'})

def a_star(start):
	elevator = 1
	path = [start]
	frontier = [(heuristic(start), start, path)]
	explored = [start]
	while frontier:
		f, floors, path = frontier.pop(0)
		if floors == GOAL:
			return len(path) - 1
		for child in children(floors, elevator):
			addedCost = 1
			newFloors, elevator = child[0], child[1]
			if newFloors not in explored:
				frontier.append((heuristic(newFloors) + 1 + len(path), newFloors, path + [newFloors]))
				explored[newFloors] = 1 + len(path)
			elif newFloor in explored and explored[child] > 1 + len(path):
				frontier.append((heuristic(newFloors) + 1 + explored[floors], newFloors, path + [newFloors]))
				explored[newFloors] = 1 + explored[floors]

	return float('inf')

def children(floors, elevator):
	currentFloor = floors[elevator]
	children = []
	if elevator < 3:
		pass
	if elevator > 0:
		pass
	return children

def isLegal(floors, elevator):
	if not floors[elevator]:
		return False
	for floor in floors:
		for item in floors[floor]:
			if item[2] == 'C' and hasGenerator(floors[floor]): #if it's a cell
				if (item[:2] + "G") not in floors[floor]:
							return False
	return True

def hasGenerator(floor):
	for item in floor:
		if item[2] == "G": # is generator
			return True
	return False

def heuristic(floors):
	return 10 - len(floors[3])

def printFloors(floors):
	for i in range(4, 0, -1):
		print ("F" + str(i), end = " ")
		for item in floors[i]:
			print (item, end = " ")
		print ()

def main():
	floors = ({'PrG', 'PrC'},
			  {'CoG', 'CuG', 'RuG', 'PlG'},
			  {'CoC', 'CuC', 'RuC', 'PlC'},
			  set())

	print (a_star(floors))

if __name__ == '__main__':
	main()