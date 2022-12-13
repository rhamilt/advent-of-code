from functools import cmp_to_key

def cmp_packets(p1, p2):
    i = 0
    while i < len(p1):
        # If i has exceeded p2 length, we know that p1 must be "larger" than p2 (ie. not in right
        # order for part 1)
        if i >= len(p2): return 1

        if type(p1[i]) == int and type(p2[i]) == int:
            # If it is neither of these, they're equal and we keep going
            if p1[i] < p2[i]: return -1
            elif p1[i] > p2[i]: return 1
        else:
            newp1 = p1[i] if type(p1[i]) == list else [p1[i]]
            newp2 = p2[i] if type(p2[i]) == list else [p2[i]]
            result = cmp_packets(newp1, newp2)
            if result != 0: return result
        i += 1

    # If p1 has ended before p2 and we have confirmed they are all even, then we say that it is
    # "smaller", meaning right order for part 1
    if i < len(p2): return -1
    # If p1 has ended at the same time as p2 and we have confirmed they are all even, then we say
    # that they are equal, and return a 0. We know that we have not exceeded p2 because that is
    # covered in the while
    return 0

lines = open("13.txt").read().strip().split("\n\n")

packets = []
valid_packets = []
for l in range(len(lines)):
    packets += list(map(eval, lines[l].split('\n')))
    # See how the last two packets compare
    if cmp_packets(*packets[-2:]) == -1: valid_packets.append(l + 1)

# Part 1: I had the right idea, but I just have to be resigned to the fact that I am slow
print (sum(valid_packets))

# I'm only writing it this way because technically it makes it easier to try out other divider
# packets
div_packet1 = [[2]]
div_packet2 = [[6]]
packets += [div_packet1, div_packet2]
packets.sort(key=cmp_to_key(lambda a, b: cmp_packets(a, b)))
# Part 2: This took me longer than I would have liked, but I am at least happy that I picked up the
# comparator idea almost instantly (I was doing a similar setup anyway). I made a small mistake
# by returning the wrong value if p1 was longer than p2, but eventually figured that out
print ((packets.index(div_packet1) + 1) * (packets.index(div_packet2) + 1))
