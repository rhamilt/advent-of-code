import copy
def reverse(arr, index, length):
	sublist = []
	for i in range(index,index+length):
		sublist.append(arr[i % len(arr)])
	reverse = list(reversed(sublist))
	j=0
	for i in range(index,index+length):
		arr[i % len(arr)] = reverse[j]
		j+=1
	
	return arr

#Day 10
with open('day10.txt') as infile:
	lengths = map(int, list(infile.read().split(',')))

arr = [n for n in range(256)]
index = 0
skip_size = 0

for length in lengths:
	arr = reverse(arr, index, length)
	index = (index + length + skip_size) % len(arr)
	skip_size += 1

print (arr[0]*arr[1])

#part 2
lengths = [ord(char) for char in open('day10.txt').read().strip()] + [17, 31, 73, 47, 23]
arr = [n for n in range(256)]
index = 0
skip_size = 0

for i in range (64):
	for length in lengths:
		arr = reverse(arr, index, length)
		index = (index + length + skip_size) % len(arr)
		skip_size += 1

xor_arr = []
for i in range(16):
	xor_sum = arr[i*16]
	for j in range(1, 16):
		xor_sum = xor_sum ^ arr[i*16 + j]
	xor_arr.append(xor_sum)

print (bytes(xor_arr).hex())
