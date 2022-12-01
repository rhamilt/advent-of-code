import re

lines = open("14.txt").read().split("\n")

# Apply the mask to a given value. `floating` applies to the second part of the puzzle and
# determines whether or not we return the string with X in it like in the second puzzle
def apply_mask(val, mask, floating=False):
    str_val = "{0:0{width}b}".format(val, width=len(mask))
    new_val = ""
    for d in range(len(mask)):
        # If we are not in part 2, we had the original value bit if the mask is `X`
        # If we are in part 2, we add the original value if the bit of the mask is `0`
        # Otherwise, we just add the value from the mask
        if (mask[d] == "X" and not floating) or (mask[d] == "0" and floating):
            new_val += str_val[d]
        else:
            new_val += mask[d]

    return int(new_val, 2) if not floating else new_val

def possible_addresses(masked_addr):
    possible_addresses = []
    x_count = masked_addr.count("X")

    # We will have 2^n different addresses where n is the number of floating bits in the mask
    for i in range(2**x_count):
        # We want to replace the different X's with every possible combination of bits.
        # Here we get a string of the bits of i and replace the Xs with that string in order and
        # add it to our possibles
        rep_string = '{0:0{width}b}'.format(i, width=x_count)
        new_addr = ""
        rep_idx = 0
        for d in range(len(mask)):
            if masked_addr[d] == "X":
                new_addr += rep_string[rep_idx]
                rep_idx += 1
            else:
                new_addr += masked_addr[d]
        possible_addresses.append(new_addr)

    return possible_addresses

memory = {}
mask = ""
for line in lines:
    if re.search('mask', line):
        mask = line.split(" = ")[1]
    else:
        m = re.match(r'mem\[(\d+)\] = (\d+)', line)
        addr, val = int(m.group(1)), int(m.group(2))
        memory[addr] = apply_mask(val, mask)

# Part 1: Went pretty quickly, no major issues
print (sum(memory.values()))

memory = {}
mask = ""
for line in lines:
    if re.search('mask', line):
        mask = line.split(" = ")[1]
    else:
        m = re.match(r'mem\[(\d+)\] = (\d+)', line)
        addr, val = int(m.group(1)), int(m.group(2))
        masked_addr = apply_mask(addr, mask, floating=True)
        for possible_addr in possible_addresses(masked_addr):
            memory[possible_addr] = val

# Part 2: Didn't realize that a `0` in the mask didn't overwrite the value to a zero, but rather 
# kept the bit the same. Spent some time on that.
print (sum(memory.values()))