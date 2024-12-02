lines = open("2.txt").readlines()

def safe(report):
    diffs = list(map(lambda x: x[1] - x[0], zip(report[:-1], report[1:])))
    return (all(map(lambda x: x < 0, diffs)) or \
           all(map(lambda x: x > 0, diffs))) and \
           all(map(lambda x: abs(x) > 0 and abs(x) < 4, diffs))

def safe_with_dampener(report):
    return any(safe(report[:i] + report[i+1:]) for i in range(len(report)))

# part 1: didnt realize both conditions had to be true
print (sum(safe(list(map(int, line.split()))) for line in lines))
# part 2: pretty nifty i think
print (sum(safe_with_dampener(list(map(int, line.split()))) for line in lines))
