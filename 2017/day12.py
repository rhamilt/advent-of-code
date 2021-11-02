#Day 12
from re import match

with open('day12.txt') as infile:
	programs = {}
	for line in infile:
		m = match(r'(\d+) <-> (.*)\s', line)
		programs[m.group(1)] = m.group(2).split(', ')

visited = {'0'}
q = programs['0']

while q:
	curr = q.pop()
	visited.add(curr)
	for program in programs[curr]:
		if program not in visited:
			q.append(program)

print (len(visited))

#part 2
with open('day12.txt') as infile:
	programs = {}
	for line in infile:
		m = match(r'(\d+) <-> (.*)\s', line)
		programs[m.group(1)] = m.group(2).split(', ')
count = 0
while programs:
	visited = {list(programs.keys())[0]}
	#print (visited)
	q = programs[list(programs.keys())[0]]

	while q:
		curr = q.pop()
		visited.add(curr)
		for program in programs[curr]:
			if program not in visited:
				q.append(program)

	#print (visited)
	for program in visited:
		#print(program)
		programs.pop(program)
	count += 1

print (count)

