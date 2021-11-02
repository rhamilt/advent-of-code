DIRECS = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}

instrucs = list(map(str.strip, open('2.txt', 'r').readlines()))

code = ''
keypad = [['1','2','3'],['4','5','6'],['7','8','9']]
idx = [1,1]
for instruc in instrucs:
	for direc in instruc:
		idx[0] = max(0, min(idx[0] + DIRECS[direc][0], 2))
		idx[1] = max(0, min(idx[1] + DIRECS[direc][1], 2))
	code += keypad[idx[0]][idx[1]]

#print (code) #part 1: got it first try, felt like a loser for using if statements, went back and did this more cool way

code = ''
keypad = [
['0', '0', '1', '0', '0'],
['0', '2', '3', '4', '0'],
['5', '6', '7', '8', '9'],
['0', 'A', 'B', 'C', '0'],
['0', '0', 'D', '0', '0']
]
idx = [2, 0]

for instruc in instrucs:
	for direc in instruc:
		temp = [idx[0], idx[1]]
		idx[0] = max(0, min(idx[0] + DIRECS[direc][0], 4))
		idx[1] = max(0, min(idx[1] + DIRECS[direc][1], 4))
		if keypad[idx[0]][idx[1]] == '0': idx = [temp[0], temp[1]]
	code += keypad[idx[0]][idx[1]]

print (code) #part 2: similar to part 1, made a new keypad and added if statement. Messed up originally by not changing max index