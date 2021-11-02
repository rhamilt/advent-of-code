import re

strs = list(map(str.strip, open('5.txt', 'r').readlines()))
good_strs = []
for str in strs:
	if re.search(r'^(?!\w*ab)(?!\w*xy)(?!\w*cd)(?!\w*pq)(?=\w*(\w)\1)(?=(\w*[aeiou]){3})\w+$', str):
		good_strs.append(str)
print (len(good_strs)) #part 1: took me a while for some reason

good_strs = []
for str in strs:
	if re.search(r'^(?=\w*(\w\w)\w*\1)(?=\w*(\w)\w\2)\w+$', str):
		good_strs.append(str)
print (len(good_strs)) #part 2: spent a little bit of time figuring out that second capture group was \2 not \1