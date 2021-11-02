#Day 5
with open('day5.txt', 'r') as infile:
	steps = [int(line) for line in infile]

index = 0
count = 0

while index >= 0 and index < len(steps):
	prev_index = index
	index += steps[index]
	steps[prev_index] += 1 
	count += 1

print (count)

#part 2
with open('day5.txt', 'r') as infile:
	steps = [int(line) for line in infile]

index = 0
count2 = 0

while index >= 0 and index < len(steps):
	prev_index = index
	index += steps[index]
	steps[prev_index] += 1 if steps[prev_index] < 3 else -1
	count2 += 1

print (count2)