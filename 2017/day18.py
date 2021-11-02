#Day 18
from re import search
ALPHA = 'abcdefghijklmnopqrstuvwxyz'

directions = list(map(str.strip,open('day18.txt').readlines()))
registers = {}

prev_freq = 0
idx = 0

while 1:
	s = search(r'(\w\w\w) (\w+) (\w+)?', directions[idx])
	cmd = s.group(1)
	target = s.group(2)
	if target not in registers and target in ALPHA:
		registers[target] = 0
	if s.group(3):
		if s.group(3) in ALPHA:
			amount = registers[s.group(3)]
		else:
			amount = int(s.group(3))
	if cmd == 'snd':
		prev_freq = registers[target]
	elif cmd == 'set':
		registers[target] = amount
	elif cmd == 'add':
		registers[target] += amount
	elif cmd == 'mul':
		registers[target] *= amount
	elif cmd == 'mod':
		registers[target] = registers[target] % amount
	elif cmd == 'rcv':
		if prev_freq != 0:
			print (prev_freq)
			break
	if cmd == 'jgz':
		if target in ALPHA:
			if registers[target] > 0:
				idx += amount
			else: idx += 1
		else:
			if int(target) > 0:
				idx += amount
			else: idx += 1
	else:
		idx += 1