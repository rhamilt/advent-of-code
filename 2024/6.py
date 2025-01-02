G = open("6.txt").read().splitlines()
G = {(r, c): G[r][c] for r in range(len(G)) for c in range(len(G[r]))}

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pos = [(r, c) for (r, c), v in G.items() if v == "^"][0]

def ns(r, c, d): return r + D[d % len(D)][0], c + D[d % len(D)][1]

def walk2uh(r, c, g):
    d = 0
    path = set()
    while (r, c, d % len(D)) not in path:
        path.add((r, c, d % len(D)))
        if ns(r, c, d) not in g:
            return path, False
        if g[ns(r, c, d)] == "#":
            d += 1
        else:
            r, c = ns(r, c, d)
    return path, (r, c, d % len(D)) in path

path = {(r, c) for r, c, _ in walk2uh(*pos, G)[0]}
print (len(path))

# wanted to join with |, but my dev desk is running python 3.7 not >3.9
# this is also kind of slow but idk how to do it faster
print (sum([walk2uh(*pos, {**G,  **{co: '#'}})[1] for co in path if co != pos]))
