lines = []
with open("day2_input.txt", 'r') as infile:
	for line in infile:
		if '\n' in line:
			lines.append(line[:len(line)-1])
		else:
			lines.append(line)
#Part 1
count2 = 0
count3 = 0
boxes = []
for line in lines:
	freq_table = {}
	for char in line:
		if char in freq_table:
			freq_table[char] += 1
		else:
			freq_table[char] = 1
	if 2 in freq_table.values():
		count2 += 1
		boxes.append(line)
	if 3 in freq_table.values():
		count3 += 1
		if line not in boxes:
			boxes.append(line)
print (count2*count3)
#Part 2
duplicates = []
for line1 in range(len(boxes)):
	for line2 in range(line1 + 1,len(boxes)):
		diff = 0
		for i in range(len(boxes[line1])):
			if boxes[line1][i] != boxes[line2][i]:
				diff += 1
		if diff == 1:
			duplicates.append(boxes[line1])
			duplicates.append(boxes[line2])
print (duplicates)