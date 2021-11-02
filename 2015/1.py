instruc = list(open('1.txt', 'r').read())
codes = [1 if code == '(' else -1 for code in instruc]
print(sum(codes)) #part 1 (i know i could put codes list in the sum but making variable for p2)

#part 2
floor = 0
for code in range(len(codes)):
	floor += codes[code]
	if floor == -1:
		print(code+1)
		break