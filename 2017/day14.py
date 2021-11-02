#Day 14
INPUT = "nbysizxe"

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

def knothash(key):
	lengths = [ord(char) for char in key] + [17, 31, 73, 47, 23]
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

	return (bytes(xor_arr).hex())

def bfs(arr, r, c, num):
	if arr[r][c] != 1:
		return
	else:
		arr[r][c] = num
		if r > 0:
			bfs(arr, r - 1, c, num)
		if c > 0:
			bfs(arr, r, c - 1, num)
		if r < 127:
			bfs(arr, r + 1, c, num)
		if c < 127:
			bfs(arr, r, c + 1, num)

grid = []

for i in range(128):
	key = INPUT + '-' + str(i)
	hex_string = knothash(key)
	binary_string = '{:0128b}'.format(int(hex_string, 16))
	grid.append(list(map(int,list(binary_string))))

print (sum(sum(row) for row in grid))

#part2
curr_num = 2
count = 0

for r in range(128):
	for c in range(128):
		if grid[r][c] == 1:
			bfs(grid, r, c, curr_num)
			curr_num += 1
			count += 1

print (count)