import re

inp = open("3.txt").read()

p1_match = r'mul\((\d{1,3}),(\d{1,3})\)'
# part 1: easily
print (sum(int(a) * int(b) for a, b in re.findall(p1_match, inp)))

p2_match = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
valid = True
tot = 0
for m in re.finditer(p2_match, inp):
    if "do" in m.group():
        valid = m.group() == "do()"
    else:
        if valid: tot += int(m.group(1)) * int(m.group(2))

# part 2: easily
print (tot)
