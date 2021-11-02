OUTPUT = 19690720
def calc_output(nums, noun, verb):
	nums[1] = noun 
	nums[2] = verb
	idx = 0
	while 1:
		opcode = nums[idx]
		if opcode == 1:
			nums[nums[idx+3]] = nums[nums[idx+1]]+nums[nums[idx+2]]
			idx = (idx+4)%len(nums)
		elif opcode == 2:
			nums[nums[idx+3]] = nums[nums[idx+1]]*nums[nums[idx+2]]
			idx = (idx+4)%len(nums)
		else:
			return nums[0]

with open('day2.txt', 'r') as infile:
	temp_nums = list(map(int, infile.read().split(',')))
	nums = [num for num in temp_nums]
	#Part 1 ( Took very long time to figure out problem and then made mistake of add/mult two params instead of nums at those indices :( )
	print (calc_output(nums, 12, 2))

	#Part 2 (Took a long time to figure out what they were asking for.)
	for noun in range(0, 99):
		for verb in range(0,99):
			if calc_output([num for num in temp_nums], noun, verb) == OUTPUT:
				print (100*noun+verb)
