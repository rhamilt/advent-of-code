import re

def recur(str, multiplier):
	if '(' not in str:
		return (multiplier*len(str))

	idx = 1
	total = 0

	while idx < len(str):
		s = re.search(r'^(\d+)x(\d+)', str[idx:])
		length = int(s.group(1))
		mult = int(s.group(2))
		idx = str[idx:].index(')') + idx + 1
		total += recur(str[idx:idx+length], multiplier*mult)
		idx += length + 1

	return total

inp = open('9.txt', 'r').read()

idx = 1
out = ''

while idx < len(inp):
	s = re.search(r'^(\d+)x(\d+)', inp[idx:])
	length = int(s.group(1))
	mult = int(s.group(2))
	idx = inp[idx:].index(')') + idx + 1
	for i in range(mult):
		out += inp[idx: idx+length]
	idx += length + 1

print (str(len(out))) #part 1: got it relatively quick, stumbled a little bit on the fact that length can be from 1 to 4 digits

idx = 1
p2_out = 0
multiplier = 1

while idx < len(inp):
	s = re.search(r'^(\d+)x(\d+)', inp[idx:])
	length = int(s.group(1))
	mult = int(s.group(2))
	idx = idx + inp[idx:].index(')') + 1
	p2_out += recur(inp[idx:idx+length], mult)
	idx += length + 1
#																																		 v
print (p2_out) #part 2: took several months of between parts 1 and 2, took a long time to get, can't handle lone characters: eg. (3x3)abcY
