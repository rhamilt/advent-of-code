lines = open("14.txt").read().strip().split("\n")

rock = set()
for line in lines:
    points = [list(map(int, point.split(','))) for point in line.split(' -> ')]
    for i in range(1, len(points)):
        [x1, y1], [x2, y2] = points[i-1:i+1]
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                rock.add((x, y))

def simulate_sand(rock, infinite_floor=False):
    sand = set()
    max_cave_level = max(rock, key=lambda x: x[1])[1]

    while True:
        falling_sand = (500, 0)
        can_fall = True

        while can_fall:
            # Different possible positions for the falling sand
            down = (falling_sand[0], falling_sand[1] + 1)
            left = (falling_sand[0] - 1, falling_sand[1] + 1)
            right = (falling_sand[0] + 1, falling_sand[1] + 1)

            if down not in rock and down not in sand:
                falling_sand = down
            elif left not in rock and left not in sand:
                falling_sand = left
            elif right not in rock and right not in sand:
                falling_sand = right
            else:
                # Here we are blocked and must drop a new grain of sand
                can_fall = False
                sand.add(falling_sand)

            # If we have fallen past the deepest point in the cave, we break either way
            if falling_sand[1] > max_cave_level:
                # If we're in part 2 with the infinite floor, we add the sand to the list because
                # it has now hit the infinite floor below the max level.
                # Otherwise we just exit because we know it will fall infinitely
                if infinite_floor:
                    sand.add(falling_sand)
                    can_fall = False
                break

        # If the sand can still fall into the abyss, we know we're in part 1 and must exit
        # If the sand has reached the spout, it cannot fall anymore and we must exit
        if can_fall or falling_sand == (500, 0): break

    print (len(sand))

# Part 1: Lord bozo takes the crown again. Not only was I mind-numbingly slow, I also somehow was
# not using my full input. Meaning my code was not giving the right response even tho it was
# correct.
simulate_sand(rock)
# Part 2: Pretty easy, just put sand in the sand set if we reached below the max cave level
simulate_sand(rock, infinite_floor=True)
