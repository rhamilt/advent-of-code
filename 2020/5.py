lines = map(str.strip, open('5.txt').readlines())

ids = set()
for line in lines:
    line = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    ids.add(int(line, 2))

# part 1: I remember doing this one in ruby and how I missed that it was binary, safe to say I
# didn't want to make that same mistake this time
print (max(ids))

for i in range(max(ids)):
    if i not in ids:
        if i - 1 in ids and i + 1 in ids:
            # part 2: pretty easy
            print (i)