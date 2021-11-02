from re import search

def parse(line):
	ingredient = line[:line.index(':')]
	qualities_strings = line[line.index(':')+2:].split(', ')
	qualities = []
	for q in qualities_strings:
		s = search(r'(\w+) (-?\d+)', q)
		qualities.append(int(s.group(2)))
	return ingredient, qualities #qualities always in the format: capacity, durability, flavor, texture

lines = list(map(str.strip, open('15.txt', 'r').readlines()))
properties = {}

for line in lines:
	ingredient, qualities = parse(line)
	properties[ingredient] = qualities

scores = []
cal_scores = []
for s in range(100):
	for b in range(100-s):
		for ch in range(100-s-b):
			ca = 100-s-b-ch
			stats = []
			for i in range(4):
				stats.append(s*properties["Sprinkles"][i] + b*properties["Butterscotch"][i] + ch*properties["Chocolate"][i] + ca*properties["Candy"][i])
			cal_sum = s*properties["Sprinkles"][4] + b*properties["Butterscotch"][4] + ch*properties["Chocolate"][4] + ca*properties["Candy"][4]
			if min(stats) > 0:
				scores.append(stats[0]*stats[1]*stats[2]*stats[3])
				if cal_sum == 500:
					cal_scores.append(stats[0]*stats[1]*stats[2]*stats[3])
print (max(scores)) #part 1: took a minute to figure out non-brute force way, decided to do that anyway :(
print (max(cal_scores)) #part 2: pretty simple addition of if statement, still sad that i had to brute force :(


