import copy
def calcTotal(plants):
	total = 0	
	for plant in range(len(plants)):
		if plants[plant] == '#':
			total += plant-50
	return total

with open('day12_input.txt', 'r') as infile:
	lines = infile.readlines()
	initial = lines[0][lines[0].index(':')+2:].strip()
	legend = {}
	for i in range(2, len(lines)):
		legend[lines[i][:lines[i].index("=")-1]] = lines[i][len(lines[i])-2]

plantLine = 50*'.' + initial + 100*'.'
generations = []
for i in range(500):
	temp = plantLine
	for plant in range (2, len(plantLine)-2):
		group = temp[plant-2] + temp[plant-1] + temp[plant] + temp[plant+1] + temp[plant+2]
		plantLine = plantLine[:plant] + legend[group] + plantLine[plant+1:]
	total = calcTotal(plantLine)
	generations.append(total)

print(generations)
print (calcTotal(plantLine))