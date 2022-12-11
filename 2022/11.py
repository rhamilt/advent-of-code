import re
from functools import reduce

lines = open("11.txt").read().strip().split("\n\n")

ops = [monkey[2][monkey[2].index('old'):] for monkey in map(lambda s: s.split('\n'), lines)]
divisors = [int(monkey.split('\n')[3].split()[-1]) for monkey in lines]
true = [int(monkey.split('\n')[4].split()[-1]) for monkey in lines]
false = [int(monkey.split('\n')[5].split()[-1]) for monkey in lines]

def play(n, monkeys, div_by):
    counts = [0] * len(monkeys)
    prod_divisors = reduce(lambda a, b: a * b, divisors)
    for _ in range(n):
        for i in range(len(monkeys)):
            counts[i] += len(monkeys[i])
            while monkeys[i]:
                # `old` is necessary for eval to work properly
                old = monkeys[i].pop(0)
                item = eval(ops[i]) % prod_divisors // div_by
                if item % divisors[i] == 0:
                    monkeys[true[i]].append(item)
                else:
                    monkeys[false[i]].append(item)
    counts.sort()
    return counts[-1] * counts[-2]

def parse_monkeys(lines):
    return [list(map(int, re.findall(r'\d+', monkey.split("\n")[1]))) for monkey in lines]

# Part 1: My fixation with parsing never ends. I should have just hard coded ops to start. I was
# getting all sorts of issues with lambda function parsing that I did not understand. The functions
# stored in the list kept changing, and it was impossible for me to figure out why. I am still very
# dissatisfied with the way that all turned out, I hate hardcoding input. I ended up using eval
# (which is mega slow) in order to get this to not be hardcoded
print (play(20, parse_monkeys(lines), div_by=3))
# Part 2: I did this the day after because I didn't want to think about it at 1am. Definitely an
# interesting and intuitive trick, but I did not pick up on it right away. Once I figured out that
# the goal was to keep the numbers down, it came pretty quick
print (play(10000, parse_monkeys(lines), div_by=1))
