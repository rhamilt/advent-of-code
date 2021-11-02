class Node():
	def __init__(self, pre, post, val):
		self.pre = pre
		self.post = post
		self.val = val

with open('day9_input.txt', 'r') as infile:
	line = infile.read().split()
	playerCount = int(line[0])
	lastMarble = 100*int(line[6])

scores = []
for i in range(playerCount):
	scores.append(0)

head = Node(None, None, 0)
head.pre = head
head.post = head
currMarble = head
currPlayer = 0
for marble in range(1, lastMarble+1):
	if marble % 23 == 0:
		scores[currPlayer] += marble
		for i in range(7):
			currMarble = currMarble.pre
		scores[currPlayer] += currMarble.val
		currMarble.pre.post = currMarble.post
		currMarble.post.pre = currMarble.pre
		currMarble = currMarble.post
	else:
		currMarble = currMarble.post
		temp = Node(currMarble, currMarble.post, marble)
		currMarble.post.pre = temp
		currMarble.post = temp
		currMarble = currMarble.post
	'''
	print("%d: [%d]" % (marble, currPlayer), end=': ')
	print (head.val, end=' ')
	tempPointer = head.post
	while tempPointer != head:
		print (tempPointer.val, end=' ')
		tempPointer = tempPointer.post
	print ()
	'''
	if currPlayer == playerCount - 1:
		currPlayer = 0
	else:
		currPlayer += 1
	#print (scores)

print (max(scores))