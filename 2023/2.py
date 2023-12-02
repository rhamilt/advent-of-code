from collections import defaultdict
from functools import reduce

lines = open("2.txt").read().strip().split("\n")

colors = {"red": 12, "green": 13, "blue": 14}

total = 0
for i, line in enumerate(lines):
    [_, s] = line.split(": ")
    game = i + 1
    rounds = s.split("; ")
    valid = True
    for round in map(lambda x: x.split(", "), rounds):
        for marbles in round:
            [num, color] = marbles.split()
            valid &= colors[color] >= int(num)
    if valid: total += game

print (total)

total = 0
for line in lines:
    power = 1
    mins = defaultdict(int)
    [_, s] = line.split(": ")
    rounds = s.split("; ")
    for round in map(lambda x: x.split(", "), rounds):
        for marbles in round:
            [num, color] = marbles.split()
            mins[color] = max(int(num), mins[color])

    total += reduce(lambda x,y: x*y, mins.values())

print (total)
