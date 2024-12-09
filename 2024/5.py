from functools import cmp_to_key
from re import findall
from collections import defaultdict

[rules_str, pages_str] = open("5.txt").read().split("\n\n")

rules = defaultdict(list)
for a, b in findall(r'(\d+)\|(\d+)', rules_str):
    rules[a].append(b)

pages = list(map(lambda s: s.split(","), pages_str.split()))

# Original solution was like this for p1
'''
def valid(page):
    seen = set()
    for x in page:
        for y in seen:
            if x not in rules[y]:
                return False
        seen.add(x)
    return True

print (sum(int(page[len(page)//2]) * valid(page) for page in pages))
'''

p1 = 0
p2 = 0
for p in pages:
    sp = sorted(p, key=cmp_to_key(lambda x, y: -(x in rules[y])), reverse=True) 
    med = int(sp[len(p)//2])
    if p == sp:
        p1 += med
    else:
        p2 += med
print (p1)
print (p2)
