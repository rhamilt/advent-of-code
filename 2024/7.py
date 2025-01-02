import re

raw = open("7.txt").read()

def do(eq, l):
    if len(l) == 1:
        return eq if l[0] == eq else 0
    return eq if do(eq, [l[0] + l[1]] + l[2:]) or do(eq, [l[0] * l[1]] + l[2:]) or do(eq, [int(str(l[0]) + str(l[1]))] + l[2:]) else 0

# brute force idgaf
print (sum(do(int(eq), list(map(int, vs.split()))) for eq, vs in re.findall(r'(\d+): (.*)', raw)))
