from collections import Counter

nums = sorted(list(map(int, open('10.txt').read().split('\n'))))

nums = [0] + nums + [nums[-1] + 3]

diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]

# Part 1: Quite simple to count the diffs
print (diffs.count(1) * diffs.count(3))

routes = Counter({0: 1})

for num in nums:
    routes[num + 1] += routes[num]
    routes[num + 2] += routes[num]
    routes[num + 3] += routes[num]

# part 2: credit to u/kuar_virunurm from r/aoc solution thread. I spend a long time thinking about
# this, even though i've already done it, and decided I didn't want to get myself any further
# entangled with it. very elegant solution that relies on the fact that to get our final result we
# don't actually care about update adaptor values that don't really exist
print (routes[nums[-1]])