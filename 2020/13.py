lines = open("13.txt").read().split("\n")

earliest = int(lines[0])
buses = lines[-1].split(",")
ids = [int(x) for x in buses if x != "x"]

time = 0
while True:
    possible_departures = [x for x in ids if (earliest + time) % x == 0]
    if len(possible_departures) > 0:
        # Part 1: It took me a surprisingly long time to figure out what I actually had to do here
        print (possible_departures[0] * time)
        break
    time += 1

increment = ids[0]
time = 0
for i in range(1, len(buses)):
    if buses[i] == "x": continue
    while (time + i) % int(buses[i]) != 0:
        time += increment
    increment *= int(buses[i])

# Part 2: I didn't really want to think about this again so I copied my ruby solution
print (time)