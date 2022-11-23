import functools

groups = open("6.txt").read().strip().split("\n\n")

count = 0
for group in groups:
    count += len(set(''.join(group.split())))

# part 1: did this easily and quickly
print (count)

count = 0
for group in groups:
    people = group.split()
    count += len(functools.reduce(lambda a, b: set(a).intersection(set(b)), people))

# part 2: This was easy once I figured out how to reduce
print (count)