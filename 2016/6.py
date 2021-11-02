from collections import Counter

lines = open('6.txt', 'r').read().split('\n')

print (''.join([Counter(col).most_common()[0][0] for col in [[line[i] for line in lines] for i in range(8)]]))
#part 1: knew i could make this a 1 line, had to deconstruct it before i could get it right, probably shouldnt have lol
print (''.join([Counter(col).most_common()[-1][0] for col in [[line[i] for line in lines ] for i in range(8)]]))
#part 2: using counter paid off, chose last instead of first and it took about 20 seconds