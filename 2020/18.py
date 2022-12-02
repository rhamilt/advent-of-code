from functools import reduce

lines = open("18.txt").read().strip().split("\n")

def parse(line, advanced=False):
    exp = list("".join(line.split()))
    # Replace all paren expressions
    while "(" in exp:
        start = exp.index("(")
        idx = start + 1
        stack = 0
        while stack > 0 or exp[idx] != ")":
            if exp[idx] == "(":
                stack += 1
            if exp[idx] == ")":
                stack -= 1
            idx += 1
        exp = exp[:start] + [str(parse("".join(exp[start + 1: idx]), advanced))] + exp[idx + 1:]

    return advanced_math(exp) if advanced else math(exp)

# Does math in a straight line
def math(exp):
    val = int(exp[0])
    c = 1
    while c < len(exp):
        if exp[c] == "*":
            val *= int(exp[c + 1])
        else:
            val += int(exp[c + 1])
        c += 2
    return val

# Math giving + precendence over *
def advanced_math(exp):
    while "+" in exp:
        new_val = int(exp[exp.index('+') - 1]) + int(exp[exp.index('+') + 1])
        exp = exp[:exp.index("+") - 1] + [str(new_val)] + exp[exp.index("+") + 2:]
    exp = map(int, filter(lambda x: x.isalnum(), exp))
    return reduce(lambda a, b: a * b, exp)

# Part 1: Moved surprisingly quickly and easily, came up with a pretty good solution I think
print (sum(parse(line) for line in lines))
# Part 2: Another tidy solution, got tripped up because I forgot to set the `advanced` flag in
# the recursive calls
print (sum(parse(line, advanced=True) for line in lines))