import re, json

input = open('12.txt', 'r').read()

def recur(obj):
	if type(obj) is int:    return obj
	elif type(obj) is list: return sum(recur(v) for v in obj)
	elif type(obj) is dict:
		if 'red' in obj.values():
			return 0
		else: return sum(recur(v) for v in obj.values())
	else: return 0

total = sum(map(int, re.findall(r'-?\d+', input)))

print (total) #part 1: very easy, took a second to find right re method and remember to account for neg

print (recur(json.loads(input))) #part 2: took some time to learn about json library, pretty easy recursion after that