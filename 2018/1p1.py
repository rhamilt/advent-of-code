with open("day1_input.txt", 'r') as infile:
	count = 0
	for line in infile:
		count += int(line)
	print (count)