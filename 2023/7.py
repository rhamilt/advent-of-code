from collections import Counter
from functools import cmp_to_key


CARDS = "23456789TJQKA"
CARDS2 = "J23456789TQKA"


lines = open("7.txt").readlines()


def remove_wildcard(h):
    if "J" in h and len(h) > 1:
        num_J = h["J"]
        h.pop("J")
        h[max(h.keys(), key=lambda x: h[x])] += num_J


def hand_cmp(h1, h2, p2=False):
    h1, h2 = Counter(h1), Counter(h2)
    if p2: remove_wildcard(h1); remove_wildcard(h2)
    mh1, mh2 = max(h1.values()), max(h2.values())
    # Strictly more
    if mh1 != mh2: return mh1 - mh2
    # Full house vs 3 of a kind check
    if set(h1.values()) == {3, 2}:
        return 0 if set(h2.values()) == {3, 2} else 1
    elif set(h2.values()) == {3, 2}:
        return -1
    # 2 pair vs single pair check
    return list(h1.values()).count(2) - list(h2.values()).count(2)


def value_cmp(h1, h2, p2=False):
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            if not p2:
                return 1 if CARDS.index(h1[i]) > CARDS.index(h2[i]) else -1
            else:
                return 1 if CARDS2.index(h1[i]) > CARDS2.index(h2[i]) else -1
    return 0


def overall_cmp(h1, h2):
    (h1, _), (h2, _) = h1, h2
    cmp = hand_cmp(h1, h2)
    return cmp if cmp else value_cmp(h1, h2)


def overall_cmp_2(h1, h2):
    (h1, _), (h2, _) = h1, h2
    cmp = hand_cmp(h1, h2, p2=True)
    return cmp if cmp else value_cmp(h1, h2, p2=True)


hands = sorted(map(str.split, lines), key=cmp_to_key(overall_cmp))
print (sum([(i + 1) * int(h[1]) for i, h in enumerate(hands)]))

hands = sorted(map(str.split, lines), key=cmp_to_key(overall_cmp_2))
print (sum([(i + 1) * int(h[1]) for i, h in enumerate(hands)]))
