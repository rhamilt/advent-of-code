from itertools import combinations

containers = list(map(int, open('17.txt', 'r').readlines()))

sum_to_150 = []

for i in range(len(containers)):
	for i in combinations(containers, i):
		if sum(i) == 150:
			sum_to_150.append(i)

print (len(sum_to_150)) #part 1: smart enough to figure out that it was a good idea to use combinations, dumb enough to not realize you could only use a bottle once

min_len = min(map(len, sum_to_150))

sum_2_150 = [] #cheeky
for i in range(len(containers)):
	for i in combinations(containers, i):
		if sum(i) == 150 and len(i) == min_len:
			sum_2_150.append(i)

print (len(sum_2_150)) #part 2: continues to be simple addendum to code