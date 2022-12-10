lines = open("10.txt").read().strip().split("\n")

x = 1
cycles = [1]
for line in lines:
    if "addx" in line:
        cycles.append(x)
        x += int(line.split()[1])
    cycles.append(x)

# Part 1: I guess it was a very slight indexing error, but I somehow got part 1 correct on my input
# without realizing it was incorrect on the test input. Never seen that before
print (sum(cycles[i - 1] * i for i in range(20, len(cycles), 40)))

for i in range(len(cycles)):
    if i % 40 == 0: print ()
    if abs(cycles[i] - (i % 40)) < 2:
        print ("#", end="")
    else:
        print (" ", end="")
# Part 2: This took me forever. A lot of that was figuring out why my part 1 didn't work properly,
# the rest was me being stupid to realize that the CRT pixels reset to zero every 40 cycles. My
# code was working perfectly for the first row, and then not printing anything at all after, just
# because I forgot to reset it
print()