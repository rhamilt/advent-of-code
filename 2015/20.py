input = 36000000

houses = {}

for i in range(1,input//10):
	houses[i] = 0
	for j in range(1,i):
		if i % j == 0:
			houses[i] += 10*j
	if houses[i] > input:
		print (house)
		break
