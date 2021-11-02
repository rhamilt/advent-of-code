#Day 3
square = 527**2
distance_to_square = 526
input = 277678
difference = square - input
print (distance_to_square-difference)

#Part 2

spiral = [[0 for x in range(7)] for i in range(7)]

start = [3,3]

num = 1
spiral[start[0]][start[1]] = num
start[1] += 1
count = 1
switch = 1
place = 0
for x in range(25):
	num = sum([spiral[start[0]+i][start[1]+j] for i in range(-1,2) for j in range(-1,2)])
	spiral[start[0]][start[1]] = num
	if switch == 0: #right
		start[1] += 1
		place += 1
		if place == 2:
			switch += 1
	elif switch == 1:#up
		start[0] -= 1
		if place == 2:
			switch += 1
		count += 1
	elif switch == 2:#left
		start[1] -= 1
		if place == 2:
			switch += 1
	elif switch == 3:#down
		start[0] += 1
		if place == 2:
			switch = 0
			count += 1

