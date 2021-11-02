from re import search

def parse(line):
	s = search(r'^(\w+).*?(\d+).*?(\d+).*?(\d+)', line)
	reindeer, speed, duration, rest = s.group(1), int(s.group(2)), int(s.group(3)), int(s.group(4))
	return (reindeer, speed, duration, rest)

lines = list(map(str.strip, open('14.txt', 'r').readlines()))

reindeer, speeds, durations, rests, dists, points = [], [], [], [], [], []

for line in lines:
	rule = parse(line)
	reindeer.append(rule[0])
	speeds.append(rule[1])
	durations.append(rule[2])
	rests.append(rule[3])
	dists.append(0)
	points.append(0)

temp_dur, temp_rest = [w for w in durations], [w for w in rests]

for second in range(2503):
	for deer in range(len(reindeer)):
		if temp_dur[deer] > 0:
			dists[deer] += speeds[deer]
			temp_dur[deer] -= 1
			temp_rest[deer] = rests[deer] #too lazy to come up with clean way, just setting it every time lol
		elif temp_rest[deer] > 1:
			temp_rest[deer] -= 1
		elif temp_rest[deer] == 1:
			temp_rest[deer] -= 1
			temp_dur[deer] = durations[deer]
	max_dist = max(dists)
	for deer in range(len(reindeer)):
		if dists[deer] == max_dist:
			points[deer] += 1


print (max(dists)) #pretty simple, made minor regex error that caused rests to be way off

print (max(points))
