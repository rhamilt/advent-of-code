class Node():
	def __init__(self, numChildren, numMetaData, parentNode):
		self.numChildren = numChildren
		self.numMetaData = numMetaData
		self.metaValue = 0
		self.metaData = []
		self.children = []
		self.parentNode = parentNode

def recur1(ind, nums, currNode, nodes):
	if ind > len(nums):
		return nodes, ind
	for j in range(currNode.numChildren):
		numCC = int(nums[ind])
		numCMD = int(nums[ind+1])
		newNode = Node(numCC, numCMD, currNode)
		currNode.children.append(newNode)
		ind += 2
		nodes.append(newNode)
		nodes, ind = recur1(ind, nums, newNode, nodes)
	for i in range(currNode.numMetaData):
		currNode.metaData.append(int(nums[ind]))
		currNode.metaValue += int(nums[ind])
		ind += 1
	return nodes, ind

def recur2(currNode):
	if currNode.numChildren > 0:
		for child in currNode.children:
			child.metaValue = recur2(child)
		currNode.metaValue = 0
		for datum in currNode.metaData:
			if datum-1 < currNode.numChildren:
				currNode.metaValue += currNode.children[datum-1].metaValue
	return currNode.metaValue
	
def summer(nodes):
	total = 0
	for node in nodes:
		total += node.metaValue
	return total

with open('day8_input.txt', 'r') as infile:
	nums = infile.read().split()

nodes = []
nodes.append(Node(int(nums[0]), int(nums[1]), None))
nodes, length = recur1(2, nums, nodes[0], nodes)
print (summer(nodes))

#Part 2
print (recur2(nodes[0]))


