from re import search
from collections import deque
from numpy import vectorize
import random

def indices(string, substring):
	return [i for i in range(len(string)) if string[i: i+len(substring)] == substring]

def replace(string, conversions):
	for i, j in conversions:
		for k in range(len(string)):
			if string[k:k + len(j)] == j:
				y = string[:k] + i + string[k + len(j):]
				yield y
def simplify(string, conversions):
	visited = {string}
	arr = [string]
	count = 0

	while 1:
		temp = []
		for state in arr:
			for child in replace(state, conversions):
				if child in visited:
					continue
				temp.append(child)
				visited.add(child)
				break
		arr = temp
		count += 1
		if 'e' in arr:
			return count
		elif len(arr) == 0:
			random.shuffle(conversions)
			visited = {string}
			arr = [string]
			count = 0


lines = [line.strip() for line in open('19.txt', 'r')]
distinct = set()
conversions = []
orig = lines[-1][::-1]

for conversion in range(len(lines)-2):
	temp = lines[conversion].split()
	conversions.append((temp[0][::-1], temp[2][::-1]))

for substring in conversions:
	for idx in indices(orig, substring[0]):
		distinct.add(orig[:idx] + substring[1] + orig[idx+len(substring[0]):])

print (len(distinct)) #part 1: simple enough, made a couple bonehead mistakes with slicing
random.shuffle(conversions)
print (simplify(orig, conversions)) #part 2: i hate this stupid little problem i had to cheat a little bit because the stupid thing was so hard