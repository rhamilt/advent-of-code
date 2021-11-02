#Day 16
from re import search
import sys

directions = open("day16.txt").read().split(',')
arr = [chr(i) for i in range(97,113)]

for direction in directions:
	s = search(r's(\d+)', direction)
	if s:
		arr = arr[len(arr) - int(s.group(1)):] + arr[:len(arr) - int(s.group(1))]
		continue
	s = search(r'x(\d+)/(\d+)', direction)
	if s:
		temp = arr[int(s.group(1))]
		arr[int(s.group(1))] = arr[int(s.group(2))]
		arr[int(s.group(2))] = temp
	s = search(r'p(\w)/(\w)', direction)
	if s:
		ind1 = arr.index(s.group(1))
		ind2 = arr.index(s.group(2))
		temp = arr[ind1]
		arr[ind1] = arr[ind2]
		arr[ind2] = temp

print (''.join(arr))

#part 2
arr = [chr(i) for i in range(97,113)]
states = []
while 1:
	if tuple(arr) in states:
			cycle = len(states)
			print (''.join(states[int(1e9)%len(states)]))
			sys.exit(0)
	states.append(tuple(arr))
	for direction in directions:
		s = search(r's(\d+)', direction)
		if s:
			arr = arr[len(arr) - int(s.group(1)):] + arr[:len(arr) - int(s.group(1))]
			continue
		s = search(r'x(\d+)/(\d+)', direction)
		if s:
			temp = arr[int(s.group(1))]
			arr[int(s.group(1))] = arr[int(s.group(2))]
			arr[int(s.group(2))] = temp
		s = search(r'p(\w)/(\w)', direction)
		if s:
			ind1 = arr.index(s.group(1))
			ind2 = arr.index(s.group(2))
			temp = arr[ind1]
			arr[ind1] = arr[ind2]
			arr[ind2] = temp