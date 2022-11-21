lines = list(map(int,map(str.strip, open('1.txt', 'r').readlines())))

twoFound, threeFound = False, False
for i in lines:
    for j in lines:
        for k in lines:
            if i + j == 2020 and not twoFound:
                # part 1: brute force :)
                print("Part 1: " +  str(i*j))
                twoFound = True
            if i + j + k == 2020 and not threeFound:
                # part 2: brute force :)
                print("Part 2: " +  str(i*j*k))
                threeFound = True

# At the end of the day, it's much faster to write a solution that is fully O(n^2) or O(n^3) than
# to write one that has j/k starting from i. Too hard to deal with indexing when this is so easy