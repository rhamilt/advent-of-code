#Day 1
with open('day1.txt', 'r') as infile:
	input = infile.read()

sum = 0

for counter in range(-1, len(input)-1):
	if input[counter] == input[counter+1]:
		sum += int(input[counter])

print (sum)

#Part 2
sum2 = 0

for counter in range(len(input)):
	if input[counter] == input[(counter + len(input)//2) % len(input)]:
		sum2 += int(input[counter])

print (sum2)