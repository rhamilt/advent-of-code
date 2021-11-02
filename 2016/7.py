import re

lines = open('7.txt', 'r').read().split('\n')

count = 0
for line in lines:
	if re.search(r'(\w)(\w)\2\1', line):
		if not re.search(r'\[\w*(\w)(\w)\2\1\w*\]|(\w)\3\3\3', line):
			count += 1

print (count) #part 1: immediately went to regex, tried to get cute with a one line like the good old days, easier to do this

count = 1
for line in lines:
	s = re.search(r'(\w)(?!\1)(\w)\1.*\[\w*\2\1\2\w*\]|\[\w*(\w)(?!\3)(\w)\3\w*\].*\4\3\4', line)
	if s:
		if s.group(0).count('[') == s.group(0).count(']'):
			count += 1

print (count) #part 2: took me a while, realized that the first group had to be outside of brackets, hence second if