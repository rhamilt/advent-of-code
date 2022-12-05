import re
from collections import defaultdict
from copy import deepcopy

[stack_input, instrucs] = open("5.txt").read().split("\n\n")

stacks = defaultdict(lambda: [])
for line in stack_input.split('\n')[:-1]:
    stack = 1
    for i in range(1, len(line), 4):
        if line[i] != " ":
            stacks[stack].append(line[i])
        stack += 1

stacks2 = deepcopy(stacks)
for line in instrucs.split('\n'):
    m = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    quant, s1, s2 = int(m.group(1)), int(m.group(2)), int(m.group(3))

    # For part 1, we put on the reversed list
    new_stack = stacks[s1][:quant][::-1] + stacks[s2]
    stacks[s1] = stacks[s1][quant:]
    stacks[s2] = new_stack

    # For part 2, we put on the not reversed list
    new_stack = stacks2[s1][:quant] + stacks2[s2]
    stacks2[s1] = stacks2[s1][quant:]
    stacks2[s2] = new_stack

# Part 1: Again, dreadfully slow. My thoughts were all there again, but I just can't seem to
# execute any of them. Today my mistake was that I changed s1 before putting it into s2. How stupid
for i in range(1, 10):
    print (stacks[i][0], end="")
print ()

# Part 2: This part I did quickly, because coincidentally I was doing it for part 1 without
# realizing :((
for i in range(1, 10):
    print (stacks2[i][0], end="")
print ()