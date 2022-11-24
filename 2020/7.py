import re

lines = open('7.txt').read().split('\n')

def p2(bag, count, multiplier, rules):
    if len(rules[bag]) == 0: return count
    bags_in_this_bag = 0
    for sub_bag in rules[bag]:
        num_sub_bags = multiplier * int(sub_bag[0])
        bags_in_this_bag += p2(sub_bag[1], num_sub_bags, num_sub_bags, rules)
    return bags_in_this_bag + count 

rules = {}
eventually_contain = {}

for line in lines:
    split_line = line.split(" bags contain ")
    bag, sub_bags = split_line[0], ''.join(split_line[1:])
    rules[bag] = []
    for sub_bag in re.findall(r'(\d+) (\w+ \w+) bag', sub_bags):
        rules[bag].append(sub_bag)


# I could break when I see a shiny gold in the while, but I thought it would be more useful to
# create a full list of every bag
for bag, sub_bags in rules.items():
    frontier = [x for x in sub_bags]
    seen = set()
    while len(frontier) > 0:
        popped_bag = frontier.pop()[1]
        if popped_bag not in seen:
            seen.add(popped_bag)
            frontier += rules[popped_bag]
    eventually_contain[bag] = seen

# part 1: using default dict messed me up a little bit causing some hard to find bugs
print (sum(1 for x in eventually_contain.values() if "shiny gold" in x))
# part 2: Forgot to add current number of bags to number of bags in current bag
# (i understand thats confusing)
print (p2("shiny gold", 0, 1, rules))