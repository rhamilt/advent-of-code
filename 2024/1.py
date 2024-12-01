lines = list(map(str.split, open("1.txt").readlines()))
left = sorted([int(x[0]) for x in lines])
right = sorted([int(x[1]) for x in lines])

# part 1: did not realize that maps were iterators that disappeared as you iterated lol
print (sum(map(lambda x: abs(x[0] - x[1]), zip(left, right))))

# part 2: bangarang
print (sum({i: i * right.count(i) for i in left}.values()))

