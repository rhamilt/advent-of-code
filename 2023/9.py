def diffs(seq):
    return list(map(lambda x: x[1] - x[0], zip(seq[:-1], seq[1:])))


lines = open("9.txt").readlines()

vals1, vals2 = [], []
for seq in map(lambda x: list(map(int, x.split())), lines):
    ds = diffs(seq)
    seqs = [seq]
    while any(ds):
        seqs.append(ds)
        ds = diffs(ds)

    extras1, extras2 = [0], [0]
    for s in reversed(seqs):
        extras1.append(s[-1] + extras1[-1])
        extras2.append(s[0] - extras2[-1])
    vals1.append(extras1[-1])
    vals2.append(extras2[-1])

print (sum(vals1))
print (sum(vals2))
