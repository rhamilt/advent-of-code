inp = open('day4.txt', 'r').read()

lower, upper = int(inp[0:inp.index('-')]), int(inp[inp.index('-')+1:])

count1 = 0
count2 = 0
for pword in range(lower, upper+1):
	password = str(pword)
	double, rdouble, increasing = False, False, True
	for digit in range(len(password)-1):
		if int(password[digit]) > int(password[digit+1]):
			increasing = False
		if password[digit] == password[digit+1]:
			double = True
			if not (password[digit] == password[digit-1] or (digit < len(password)-2 and password[digit] == password[digit+2])):
				rdouble = True

	if double and increasing:
		count1 += 1
	if double and increasing and rdouble: #rdouble = Really Double
		count2 += 1
#Part 1: Pretty straight forward, kind of slow
print (count1)
#Part 2: Took a couple minutes to figure out how to accept passwords with both groups and doubles
print (count2)