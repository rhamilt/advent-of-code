import sys
def display(track):
	for y in range(150):
		for x in range(150):
			print (track[y][x], end='')
		print ()

track = []
carts = []
INIT_DIRECTION_TABLE = {'^': '|', 'v': '|', '<': '-', '>': '-'}
DIRECTION_TABLE = {'^': (0,-1), 'v': (0,1), '<': (-1,0), '>': (1,0)}
TURN_TABLE = {'^': ('<','^', '>'), 'v': ('>','v', '<'), '<': ('v','<', '^'), '>': ('^','>', 'v')}
CURVE_TABLE = {('^', '\\'): '<', ('^', '/'): '>', ('>', '\\'): 'v', ('>', '/'): '^', ('v', '\\'): '>', ('v', '/'): '<', ('<', '\\'): '^', ('<', '/'): '>'}
with open("day13_input.txt", 'r') as infile:
	for y in range(150):
		track.append([])
		line = infile.readline()
		x = 0
		for char in line:
			track[y].append(char)
			if char in DIRECTION_TABLE:
				carts.append([y, x, char, 1, INIT_DIRECTION_TABLE[char]])
			x += 1


#Part 1
while True:
	display(track)
	for cart in carts:
		nextX = cart[1] + DIRECTION_TABLE[cart[2]][0]
		nextY = cart[0] + DIRECTION_TABLE[cart[2]][1]
		nextValue = track[nextY][nextX]
		if nextValue == '+':
			cart[2] = TURN_TABLE[cart[2]][cart[3]%3-1]
			track[nextY][nextX] = cart[2]
			cart[3] += 1
		elif nextValue == '/' or nextValue == '\\':
			cart[2] = CURVE_TABLE[(cart[2],nextValue)]
			track[nextY][nextX] = cart[2]
		elif nextValue in DIRECTION_TABLE:
			print (nextX, nextY)
			sys.exit(0)
		else:
			track[nextY][nextX] = cart[2]
		track[cart[0]][cart[1]] = cart[4]
		cart[0] = nextY
		cart[1] = nextX
		cart[4] = nextValue
	carts = sorted(carts)
'''
count = 0
#Part 2
crashes = []
print (len(carts))
while len(carts) > 1:
	print (len(carts))
	for cart in carts:
		nextX = cart[1] + DIRECTION_TABLE[cart[2]][0]
		nextY = cart[0] + DIRECTION_TABLE[cart[2]][1]
		nextValue = track[nextY][nextX]
		if nextValue == '+':
			cart[2] = TURN_TABLE[cart[2]][cart[3]%3-1]
			track[nextY][nextX] = cart[2]
			cart[3] += 1
		elif nextValue == '/' or nextValue == '\\':
			cart[2] = CURVE_TABLE[(cart[2],nextValue)]
			track[nextY][nextX] = cart[2]
		elif nextValue in DIRECTION_TABLE:
			crashes.append((nextY, nextX))
			track[cart[0]][cart[1]] = cart[4]
			for crashedCart in carts:
				if nextY == crashedCart[0] and nextX == crashedCart[1]:
					track[nextY][nextX] = crashedCart[4]
					carts.remove(crashedCart)
			carts.remove(cart)
		else:
			track[nextY][nextX] = cart[2]
		track[cart[0]][cart[1]] = cart[4]
		cart[0] = nextY
		cart[1] = nextX
		cart[4] = nextValue
	carts = sorted(carts)
	count += 1
'''
display(track)
print (carts[0])

