#Part 1 (Separated because can't run through same file twice)
print (sum([(int(line)//3)-2 for line in open('day1.txt','r')]))
#Part 2
with open('day1.txt', 'r') as infile:
	fuel = []
	for line in infile:
		temp_fuel = int(line)
		fuel_sum = 0
		while fuel_num > 0:
			temp_fuel = max(0, int(fuel_num//3)-2)
			fuel_sum += fuel_num
		fuel.append(fuel_sum)
	print(sum(fuel))