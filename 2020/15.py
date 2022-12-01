from collections import defaultdict

lines = open("15.txt").read().strip()

def game(nums, n):
    nums_spoken = defaultdict(lambda: [])
    prev = None
    for i in range(n):
        if i < len(nums):
            nums_spoken[nums[i]].append(i)
            prev = nums[i]
        else:
            if len(nums_spoken[prev]) == 1:
                nums_spoken[0].append(i)
                prev = 0
            else:
                diff = nums_spoken[prev][-1] - nums_spoken[prev][-2]
                nums_spoken[diff].append(i)
                prev = diff
    return prev

nums = list(map(int, lines.split(',')))

# Part 1: For some reason this took me quite a while to get worked out. I understood the problem,
# but some inopportune typos made me slow as I tried to debug
print (game(nums, 2020))
# Part 2: I just let it run for 30 seconds and it got the solution, I'm not going to bother to try
# to figure out a faster one
print (game(nums, 30000000))
