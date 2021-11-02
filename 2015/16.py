INFO = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1} #copied directly from website

from re import search

def parse(line):
	s = search(r'(\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)
	sue_num = int(s.group(1))
	return sue_num, [(s.group(2), int(s.group(3))), (s.group(4), int(s.group(5))), (s.group(6), int(s.group(7)))]

lines = map(str.strip, [line for line in open('16.txt','r')])

facts = {}
for line in lines:
	sue_num, fact_dict = parse(line)
	facts[sue_num] = fact_dict #not an actual dictionary, just list of tuples lol

fits = []
for sue_num in facts:
	correct_sue = True
	for item in facts[sue_num]:
		if INFO[item[0]] != item[1]:
			correct_sue = False
	if correct_sue:
		fits.append(sue_num)
print (fits) #part 1: pretty simple, wasted like 2 minutes debugging before i realized i was printing wrong thing 

fits2 = []
for sue_num in facts:
	correct_sue = True
	for item in facts[sue_num]:
		if item[0] == 'cats' or item[0] == 'trees':
			if INFO[item[0]] >= item[1]:
				correct_sue = False
		elif item[0] == 'pomeranians' or item[0] == 'goldfish':
			if INFO[item[0]] <= item[1]:
				correct_sue = False
		else:
			if INFO[item[0]] != item[1]:
				correct_sue = False
	if correct_sue:
		fits2.append(sue_num)
print (fits2) #part 2: also very simple, just added a couple if elifs