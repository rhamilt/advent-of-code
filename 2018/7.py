class Node():
	def __init__(self, step, prereqs):
		self.prereqs = prereqs
		self.step = step
	def addPrereq(self, prereq):
		self.prereqs.append(prereq)
	def removePrereq(self, prereq):
		self.prereqs.remove(prereq)

class Worker():
	def __init__(self):
		self.busy = False
		self.project = ''
		self.timeLeft = -1


def addToAvailable(nodes, available):
	i = 0
	while i < len(nodes):
		if len(nodes[i].prereqs) == 0:
			available.append(nodes[i].step)
			nodes.pop(i)
		else:
			i += 1
	return nodes, sorted(available)

#Lookup Table
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
times = {}
for char in alpha:
	times[char] = 60 + alpha.index(char) + 1


with open("day7_input.txt", 'r') as infile:
	directions = infile.readlines()
nodes = []
for direction in directions:
	prereq = direction[direction.index(" ")+1]
	step = direction[direction.index("can")-2]
	exists = True
	for node in nodes:
		if node.step == step:
			node.addPrereq(prereq)
			exists = False
	if exists:
		nodes.append(Node(step, [prereq]))
	exists = True
	for node in nodes:
		if node.step == prereq:
			exists = False
	if exists:
		nodes.append(Node(prereq, []))

nodes, available = addToAvailable(nodes, [])

done = []
#Part 1
'''
while len(available) > 0:
	done.append(available.pop(0))
	for node in nodes:
		for finishedStep in done:
			if finishedStep in node.prereqs:
				node.removePrereq(finishedStep)
	nodes, available = addToAvailable(nodes, available)

print(''.join(done))
'''

#Part 2

workers = []
for i in range (5):
	workers.append(Worker())
time = 0
workersBusy = 0
while len(nodes) > 0 or workersBusy > 0:
	for worker in workers:
		if worker.timeLeft == 0:
			worker.busy = False
			done.append(worker.project)
			worker.timeLeft -= 1
			workersBusy -= 1
		if not worker.busy:
			if len(available) > 0:
				worker.busy = True
				worker.project = available.pop(0)
				worker.timeLeft = times[worker.project]
				workersBusy += 1
		else:
			worker.timeLeft -= 1
	for node in nodes:
		for finishedStep in done:
			if finishedStep in node.prereqs:
				node.removePrereq(finishedStep)
	nodes, available = addToAvailable(nodes, available)
	time += 1
print (time)
