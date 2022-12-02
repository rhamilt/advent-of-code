lines = open("2.txt").read().strip().split("\n")

elf_guide = "ABC"
my_guide = "XYZ"

count = 0
for line in lines:
    [them, me] = line.split()
    symbol_points = my_guide.index(me) + 1
    winner = (my_guide.index(me) - elf_guide.index(them)) % 3
    if winner == 0:
        count += 3
    elif winner == 1:
        count += 6
    count += symbol_points

# Part 1: I was just a little slow on this one, 716 overall
print (count)

count = 0
for line in lines:
    [them, me] = line.split()
    if me == "X":
        count += (elf_guide.index(them) - 1) % 3 + 1
    elif me == "Y":
        count += 3 + (elf_guide.index(them)) % 3 + 1
    else:
        count += 6 + (elf_guide.index(them) + 1) % 3 + 1

# Part 2: Took me a second to figure everything out, but then on top of that I fumbled big time by
# failing to reset my count variable, so I was just adding on to my part 1 sum
print (count)