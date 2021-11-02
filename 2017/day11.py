#Day 11
COMPASS = {'n': (-2, 0), 's': (2, 0), 'ne': (-1, 1), 'se': (1, 1), 'sw': (1, -1), 'nw': (-1, -1)}
import math
with open('day11.txt') as infile:
	directions = infile.read().split(',')

x, location = [0, 0], [0, 0]

for direction in directions:
	x[0] += COMPASS[direction][0]
	x[1] += COMPASS[direction][1]

steps = 0
while location != x:
	steps += 1
	command = ''
	if x[0] >= location[0]:
		command += 's'
	elif x[0] < location[0]:
		command += 'n'
	if x[1] < location[1]:
		command += 'w'
	elif x[1] > location[1]:
		command += 'e'
	location[0] += COMPASS[command][0]
	location[1] += COMPASS[command][1]

print (steps)

#part 2

x = [0, 0]
max_steps = 0

for direction in directions:
	location = [0, 0]
	x[0] += COMPASS[direction][0]
	x[1] += COMPASS[direction][1]
	steps = 0
	while location != x:
		steps += 1
		command = ''
		if x[0] >= location[0]:
			command += 's'
		elif x[0] < location[0]:
			command += 'n'
		if x[1] < location[1]:
			command += 'w'
		elif x[1] > location[1]:
			command += 'e'
		location[0] += COMPASS[command][0]
		location[1] += COMPASS[command][1]
	if steps > max_steps:
		max_steps = steps

print (max_steps)
