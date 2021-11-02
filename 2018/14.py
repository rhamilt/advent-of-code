input = "074501"
scores = '37'
elf1 = 0
elf2 = 1
while len(scores) < int(input) +  10:
	scores += str(int(scores[elf1]) + int(scores[elf2]))
	for ind1 in range(int(scores[elf1])+1):
		if elf1 == len(scores) - 1:
			elf1 = 0
		else:
			elf1 += 1
	for ind2 in range(int(scores[elf2])+1):
		if elf2 == len(scores) - 1:
			elf2 = 0
		else:
			elf2 += 1
last10 = ''
for i in range(len(scores)-10, len(scores)):
	last10 += scores[i]
print (last10)
#Part 2
while input not in scores:
	scores += str(int(scores[elf1]) + int(scores[elf2]))
	elf1 = (elf1 + int(scores[elf1]) + 1) % len(scores)
	elf2 = (elf2 + int(scores[elf2]) + 1) % len(scores)
print (scores.index(input))
