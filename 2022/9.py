lines = open("9.txt").read().strip().split("\n")

DIRECS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

knots = [[0, 0] for i in range(10)]
seen1 = set([(0, 0)])
seen2 = set([(0, 0)])
for line in lines:
    direc, val = line.split()
    dxy = DIRECS[direc]
    for _ in range(int(val)):
        knots[0] = [knots[0][0] + dxy[0], knots[0][1] + dxy[1]]
        for i in range(1, len(knots)):
            diff = (knots[i-1][0] - knots[i][0], knots[i-1][1] - knots[i][1])
            # This is introduced for part 2, where it is possible for a leading knot to move
            # diagonally. I got tripped up here because I accidentally used knots[i-1][0] instead
            # of knots[i-1][1] in the y position. I think this tells me that I need to start naming
            # constants X = 0, Y = 1
            if sum(map(abs, diff)) > 1 and abs(diff[0] * diff[1]) != 1:
                # We only want to change our position in a dimension if the difference between the
                # current knot and the next knot is 2 or greater. This if/else is necessary because
                # Python integer division means that 1 // -2 is -1, not the 0 I was expecting.
                # The values in diff are guaranteed to be between -2 and 2
                dx = diff[0] // -2 if abs(diff[0]) == 2 else 0
                dy = diff[1] // -2 if abs(diff[1]) == 2 else 0
                knots[i] = [knots[i-1][0] + dx, knots[i-1][1] + dy]

        seen1.add(tuple(knots[1]))
        seen2.add(tuple(knots[-1]))

# Part 1: Once again I shit the bed. My mistake today was accidentally leaving in a
# `knots[i-1][0] - 1` when the `- 1` should have been deleted after I copied it. Why must I always
# make a mistake not in logic
print (len(seen1))
# Part 2: While I am happy that I was easily able to convert my head and tail vars into a list and
# add `knots[i-1]` and `knots[i]` where appropriate, I am disappointed that it took me so long to
# realize that there are new movements possible (literally says so in the problem). My solution is
# pretty elegant I think, but I of course had another typo that I explain above
print (len(seen2))