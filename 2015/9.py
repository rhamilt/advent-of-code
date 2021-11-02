from re import search
from itertools import permutations

lines = list(map(str.strip, open('9.txt', 'r').readlines()))

dists = {}

for line in lines:
	s = search(r'(\w+) .. (\w+).+?(\d+)', line)
	start, end, dist = s.group(1), s.group(2), int(s.group(3))
	if start not in dists:
		dists[start] = []
	dists[start].append((end, dist))
	if end not in dists:
		dists[end] = []
	dists[end].append((start, dist))

route_lengths = []
for route in permutations(dists.keys()):
	leg_lengths = []
	for stop in range(len(route)-1):
		next = route[stop+1]
		for place in dists[route[stop]]:
			if place[0] == next:
				leg_lengths.append(place[1])
				break
	route_lengths.append(sum(leg_lengths))

print (min(route_lengths)) #part 1: thank god i found out there was a permutations method before i created my own, saved like 2 hrs
print (max(route_lengths)) #part 2: ultra easy, no change required since i already had all lengths
