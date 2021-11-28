def createNode(nums, i)
	numChild = nums[i]; i += 1
	numData = nums[i]; i += 1
	node = [numChild, numData]
	while numChild > 0
		nextChild, i = createNode(nums, i)
		node << nextChild
		numChild -= 1
	end
	while numData > 0
		node << nums[i]
		i += 1
		numData -= 1
	end
	return node, i
end

def metadataCount(node)
	dataStart = 2 + node[0] #Index of last child node + 1 (first metadata)
	total = node[dataStart..].sum #Total of metadata for current node
	for i in 2..dataStart-1
		total += metadataCount(node[i])
	end
	return total
end

def value(node)
	return metadataCount(node) if node[0] == 0 #BASE CASE: NO CHILDREN
	dataStart = 2 + node[0] #Index of last child node + 1 (first metadata)
	value = 0
	node[dataStart..].each do |idx|
		value += value(node[idx+1]) if idx <= node[0]
	end
	return value
end

head, i = createNode(File.open("8.txt").read.split.map(&:to_i), 0)

=begin part 1
	pretty easy, but for some reason the metadata count took me a long time. Creating the node
	structure was easy, reading it wasn't (although it should have been)
=end
p metadataCount(head)

=begin part 2
	Did not take me very long at all, pleased with how I didn't have to change anything about my structure.
=end
p value(head)