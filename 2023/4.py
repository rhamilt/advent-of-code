lines = open("4.txt").read().strip().split("\n")


def matches(line):
    [_, card] = line.split(": ")
    [a, b] = card.split(" | ")
    winning, current = set(map(int, a.split())), set(map(int, b.split()))
    return winning.intersection(current)


# casting result of 2** to an int in case there are no matches (len == 0)
print (sum(int(2**(len(matches(line)) - 1)) for line in lines))


cards = {i: 1 for i in range(len(lines))}
i = 0
for line in lines:
    for j in range(1, len(matches(line)) + 1):
        cards[i + j] += cards[i]
    i += 1


print (sum(cards.values()))
