#Day 4
with open('day4.txt', 'r') as infile:
	lines = []
	for line in infile:
		lines.append(line.split())

sum = 0
print (lines)
for line in lines:
	if len(line) == len(set(line)):
		sum += 1

print (sum)

#part 2

sum2 = 0

for line in lines:
	b = True
	if len(line) == len(set(line)):
		for word in line:
			for word2 in line:
				if word != word2:
					if set(word) == set(word2) and len(word) == len(word2):
						b = False
	else:
		b = False
	if b:
		sum2 += 1

print (sum2)