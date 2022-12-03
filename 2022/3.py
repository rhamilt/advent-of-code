lines = open("3.txt").read().strip().split("\n")

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha = alpha + alpha.upper()

count = 0
for line in lines:
    # Intersection of front and back half of the lines
    for c in set(line[:len(line)//2]).intersection(set(line[len(line)//2:])):
        count += alpha.index(c) + 1

# Part 1: Stupidly used capitalize() instead of upper() and assigned capital letters 1-26 instead
# instead of 27-52. That cost me probably 6-7 minutes
print (count)

count = 0
i = 0
while i < len(lines):
    # Intersection of next three lines
    for c in set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2])):
        count += alpha.index(c) + 1
    i += 3

# Part 2: Again stupidly used the same variable names for my index var and my character var. Caused
# a couple issues but still finished relatively quickly
print (count)