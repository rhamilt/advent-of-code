import re

lines = open("8.txt").read().split('\n')

def execute(lines):
    acc = 0
    idx = 0
    idx_seen = set()
    while idx < len(lines):
        if idx in idx_seen:
            break
        idx_seen.add(idx)
        m = re.match(r'(\w+) (\+|-)(\d+)', lines[idx])
        instruc, mult, num = m.group(1), 1 if m.group(2) == "+" else -1, int(m.group(3))
        if instruc == "acc":
            acc += mult * num
        elif instruc == "jmp":
            idx += mult * num - 1
        idx += 1
    return (acc, idx)

# part 1: Forgot to advance one after `acc` instruction
print (execute(lines)[0])

for i in range(len(lines)):
    if lines[i].startswith("acc"): continue
    temp_lines = []
    for j in range(len(lines)):
        if j == i:
            if lines[i].startswith("jmp"):
                temp_lines.append("nop" + lines[i][3:])
            elif lines[i].startswith("nop"):
                temp_lines.append("jmp" + lines[i][3:])
        else: temp_lines.append(lines[j])

    result = execute(temp_lines)

    if result[1] == len(lines):
        # part 2: Pretty straight forward, I forgot to reset the seen set for each iteration
        print (result[0])