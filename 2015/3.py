def deliver(instruc):
	houses = {(0, 0) : 1}
	current = (0, 0)
	for direc in instruc:
		code = DIRECS[direc]
		current = (current[0] + code[0], current[1] + code[1])
		if current not in houses:
			houses[current] = 0
		houses[current] += 1
	return set(houses) #only so i can union regular and robo

instruc = open('3.txt', 'r').read().strip()

DIRECS = {'v': (0, -1), '^': (0, 1), '<' : (-1, 0), '>' : (1, 0)}

print (len(deliver(instruc))) #part 1: accidentally counted all houses that received two (READ MORE CAREFULLY)

santa_instruc = instruc[::2]
robo_instruc = instruc[1::2]
print (len(deliver(santa_instruc).union(deliver(robo_instruc)))) #part 2