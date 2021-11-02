#Day 2
with open('day2.txt', 'r') as infile:
	rows = []
	for line in infile:
		rows.append([])
		nums = line.split()
		for num in nums:
			rows[-1].append(int(num))

sum = sum([int(max(row))-int(min(row)) for row in rows])

print (sum)

#Part 2

sum2 = 0

for row in rows:
	for num in row:
		for num2 in row:
			if num != num2 and num % num2 == 0:
				sum2 += num//num2
				continue

print (sum2)
	