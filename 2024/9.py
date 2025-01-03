from collections import deque, defaultdict
import heapq

inp = open("9.txt").read().strip()
written = list(map(int,inp[::2]))
free = list(map(int,inp[1::2]))

# Parse input into datastructures for p1 and p2
wd = deque()
fd = deque()
wd2 = {}
fblocks = defaultdict(list)
n = 0
for id, size in enumerate(written):
    wd2[id] = (n, size)
    for _ in range(size):
        wd.append((n, id))
        n += 1
    if id < len(free):
        heapq.heappush(fblocks[free[id]], n)
        for _ in range(free[id]):
            fd.append((n, 0))
            n += 1

while wd[-1][0] > fd[0][0]:
    wn, wi = wd.pop()
    fn, _ = fd.popleft()
    fd.append((fn, wi))
    wd.appendleft((wn, 0))

# Not really readable, the gist is that we take the highest written thing and put it into the lowest
# written thing, using queues for speed
print (sum(a * b for a, b in fd) + sum(a * b for a, b in wd))

for id in range(len(wd2) - 1, 0, -1):
    wn, size = wd2[id]
    possibles = [(fblocks[j][0], j) for j in range(size, 10) if fblocks[j]]
    if possibles:
        n, fsize = min(possibles)
        if n and n < wn:
            heapq.heappop(fblocks[fsize])
            wd2[id] = (n, size)
            if fsize != size:
                heapq.heappush(fblocks[fsize - size], n + size)

# Not readable at all, gist is that we find the lowest eligible free block using heaps, place the
# written block there, and then potentially and the fragment.
# Made a mistake because you have to use the lowest possible pos, not the tightest fitting block
print (sum(id * i for id, (n, size) in wd2.items() for i in range(n, n + size)))
