#Day 8
from re import match

with open('day8.txt') as infile:
	lines = list(map(str.strip, infile.readlines()))
	registers = {}
	for line in lines:
		m = match(r'(\w+).+if (\w+)', line)
		registers[m.group(1)] = 0
		registers[m.group(2)] = 0

for line in lines:
	m = match(r'(\w+) (dec|inc) (-?\d+) if (\w+) ([^ ]+ -?\d+)', line)
	curr_register = m.group(1)
	multiplier = 1 if m.group(2) == 'inc' else -1
	delta = int(m.group(3))
	if_statement = str(registers[m.group(4)]) + ' ' + m.group(5)
	if eval(if_statement):
		registers[curr_register] += delta*multiplier

print (max(list(registers.values())))

#part 2

registers = {}
for line in lines:
	m = match(r'(\w+).+if (\w+)', line)
	registers[m.group(1)] = 0
	registers[m.group(2)] = 0

maximum = 0

for line in lines:
	m = match(r'(\w+) (dec|inc) (-?\d+) if (\w+) ([^ ]+ -?\d+)', line)
	curr_register = m.group(1)
	multiplier = 1 if m.group(2) == 'inc' else -1
	delta = int(m.group(3))
	if_statement = str(registers[m.group(4)]) + ' ' + m.group(5)
	if eval(if_statement):
		registers[curr_register] += delta*multiplier
	if registers[curr_register] > maximum:
		maximum = registers[curr_register]

print (maximum)