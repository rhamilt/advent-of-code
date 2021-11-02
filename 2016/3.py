lines = open('3.txt', 'r').readlines()

count = 0

for line in lines:
	sides = list(map(int, line.split()))
	acceptable = True
	for i in range(3):
		if sides[i] + sides[(i+1)%3] <= sides[(i+2)%3]: acceptable = False
	if acceptable: count += 1

print(count) #part 1: got it first try, not much to say about this

count = 0
idx = 0
while idx < len(lines):
	line1 = list(map(int, lines[idx].split()))
	idx += 1
	line2 = list(map(int, lines[idx].split()))
	idx += 1
	line3 = list(map(int, lines[idx].split()))
	idx += 1
	tris = [
	[line1[0], line2[0], line3[0]],
	[line1[1], line2[1], line3[1]],
	[line1[2], line2[2], line3[2]]
	]
	for tri in tris:
		acceptable = True
		for i in range(3):
			if tri[i] + tri[(i+1)%3] <= tri[(i+2)%3]: acceptable = False
		if acceptable: count += 1

print (count) #part 2: got it first try, solution feels pretty slimy