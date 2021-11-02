from re import search
from itertools import permutations

def parse(rule):
	s = search(r'^(\w+).*(gain|lose) (\d+).*?(\w+)\.', rule)
	if s.group(2) == 'gain':
		return (s.group(1), int(s.group(3)), s.group(4)) # person, change, person that changed
	return (s.group(1), -1*int(s.group(3)), s.group(4))

def compute_happiness(rules):
	happinesses = []
	for perm in permutations(rules.keys()):
		order_happiness, idx = 0, 0
		while idx < len(perm):
			for partner in rules[perm[idx]]:
				if partner[0] == perm[(idx+1)%len(perm)]:
					order_happiness += partner[1]
					break
			for partner in rules[perm[(idx+1)%len(perm)]]:
				if partner[0] == perm[idx]:
					order_happiness += partner[1]
					break
			idx += 1
		happinesses.append(order_happiness)
	return (max(happinesses))

lines = list(map(str.strip, open('13.txt', 'r').readlines()))
rules = {}

for rule in lines:
	parsed = parse(rule)
	if parsed[0] not in rules:
		rules[parsed[0]] = []
	rules[parsed[0]].append((parsed[2], parsed[1]))


print (compute_happiness(rules)) #part 1: used permutations method from a few back, briefly forgot that the table was circular

rules['Reed'] = [(partner, 0) for partner in rules.keys()]
for person in rules:
	if person != 'Reed': rules[person].append(('Reed', 0))

print (compute_happiness(rules)) #part 2: took almost no time at all, just had to add myself to the rules list. sad that i caused overall happiness to go down