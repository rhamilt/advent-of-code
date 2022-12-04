lines = open("4.txt").read().strip().split("\n")

count = 0
count2 = 0
for line in lines:
    ranges = list(map(lambda x: list(map(int, x.split('-'))), line.split(',')))
    range1, range2 = ranges[0], ranges[1]
    if range1[0] >= range2[0] and range1[1] <= range2[1]: count += 1
    elif range2[0] >= range1[0] and range2[1] <= range1[1]: count += 1
    set1 = set(range(range1[0], range1[1] + 1))
    set2 = set(range(range2[0], range2[1] + 1))
    if len(set1.intersection(set2)) != 0: count2 += 1

# Part 1: Dreadfully slow for no reason, although I did make a big mistake of double counting ones
# that were equivalent, which cost me a few minutes
print (count)
# Part 2: Not as slow, but very silly in how I read the problem. I was looking at how many don't
# overlap rather than how many do. It's a one character change, but set me back a minute or so
# trying to figure it out.
print (count2)