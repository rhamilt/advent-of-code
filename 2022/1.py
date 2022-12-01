lines = open("1.txt").read().strip().split("\n\n")

elves = [sum(map(int, line.split())) for line in lines]

# Part 1: Figured it out easily and quickly, but accidentally adding an extra line to my input cost
# me an time because '\n'.split('\n') gives ['', ''] (not compatible with int()) while '\n'.split()
# gives []. Ended up at 449
print (max(elves))
# Part 2: Very easy and improved to 250 for part 2
print (sum(sorted(elves)[-3:]))