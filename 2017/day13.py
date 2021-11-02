#Day 13
from re import search
import itertools

def scanner(height, time):
	offset = time % ((height - 1) * 2)

	return 2 * (height - 1) - offset if offset > height - 1 else offset

lines = [line.strip() for line in open('day13.txt')]
struct = {}
for line in lines:
	s = search(r'(\d+): (\d+)', line)
	struct[int(s.group(1))] = int(s.group(2))
	scanner_pos = {int(depth): 0 for depth in struct}
	scanner_mods = {int(depth): 1 for depth in struct}

curr_index = -1
severity = 0

for picosecond in range(99):
	curr_index += 1
	if curr_index in struct:
		if scanner_pos[curr_index] == 0:
			severity += curr_index * struct[curr_index]
	for depth in scanner_pos:
		scanner_pos[depth] = (scanner_pos[depth] + scanner_mods[depth])
		if scanner_pos[depth] == 0:
			scanner_mods[depth] = 1
		elif scanner_pos[depth] == struct[depth]-1:
			scanner_mods[depth] = -1

print (severity)

#part 2

part2 = next(wait for wait in itertools.count() if not any(scanner(struct[pos], wait + pos) == 0 for pos in struct))

print (part2)
