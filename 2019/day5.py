def pmodes(pmode, x, nums):
	if pmode:
		return int(x)
	else:
		return int(nums[int(x)])

def calc_output(nums, inp):
	idx = 0
	while int(nums[idx])%100 != 99:
		command = nums[idx]
		#print(nums)
		#print(command)
		pmode1 = 0
		pmode2 = 0
		opcode = int(command[-1])
		if len(command) >= 3:
			pmode1 = int(command[-3])
		if len(command) >= 4:
			pmode2 = int(command[-4])
		if opcode == 1:
			nums[int(nums[idx+3])] = str(pmodes(pmode1, nums[idx+1], nums) + pmodes(pmode2, nums[idx+2], nums))
			idx = (idx+4)%len(nums)
		elif opcode == 2:
			nums[int(nums[idx+3])] = str(pmodes(pmode1, nums[idx+1], nums) * pmodes(pmode2, nums[idx+2], nums))
			idx = (idx+4)%len(nums)
		elif opcode == 3:
			nums[int(nums[idx+1])] = inp
			idx = (idx+2)%len(nums)
		elif opcode == 4:
			num = pmodes(pmode1, nums[idx+1], nums)
			if num != 0:
				return num
			idx = (idx+2)%len(nums)
		elif opcode == 5:
			if pmodes(pmode1, nums[idx+1], nums):
				idx = pmodes(pmode2, nums[idx+2], nums)%len(nums)
			else:
				idx = (idx+3)%len(nums)
		elif opcode == 6:
			if not pmodes(pmode1, nums[idx+1], nums):
				idx = pmodes(pmode2, nums[idx+2], nums)%len(nums)
			else:
				idx = (idx+3)%len(nums)
		elif opcode == 7:
			#print (pmodes(pmode1, nums[idx+1], nums))
			#print (pmodes(pmode2, nums[idx+2], nums))
			if pmodes(pmode1, nums[idx+1], nums) < pmodes(pmode2, nums[idx+2], nums):
				nums[int(nums[idx+3])] = '1'
			else:
				nums[int(nums[idx+3])] = '0'
			idx = (idx+4)%len(nums)
		elif opcode == 8:
			if pmodes(pmode1, nums[idx+1], nums) == pmodes(pmode2, nums[idx+2], nums):
				nums[int(nums[idx+3])] = '1'
			else:
				nums[int(nums[idx+3])] = '0'
			idx = (idx+4)%len(nums)

	return nums[0]

with open('day5.txt', 'r') as infile:
	nums = infile.readline().strip().split(',')

#Part 1: Took a while to figure out that the output was coming from whenever there was an opcode 4
print (calc_output([num for num in nums], '1'))
#Part 2: Took a while to figure out that still needed to move index for code 5 or 6 even if condition didn't change pointer
print (calc_output([num for num in nums], '5'))