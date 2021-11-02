DIRECS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

instrucs = open('1.txt','r').read().split(', ')

direc = 0
loc = [0,0]
seen = [0,0]
first = None
for instruc in instrucs:
	if instruc[0] == 'L': direc = (direc-1)%4
	else: direc = (direc+1)%4
	dist = int(instruc[1:])
	for i in range(dist):
		loc[0] += DIRECS[direc][0]
		loc[1] += DIRECS[direc][1]
		if loc not in seen: seen.append([loc[0], loc[1]])
		elif first == None: first = [loc[0], loc[1]]

print (sum(map(abs, loc))) #part 1: simple enough, got held up because i was only reading first digit, one number had three
print(sum(map(abs, first))) #part 2: got it first try, a bit messy to copy it like so, should have found a cooler way than lists.