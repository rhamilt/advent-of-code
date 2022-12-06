signal = open("6.txt").read().strip()

for c in range(0, len(signal)-4):
    if len(set(signal[c:c+4])) == 4:
        # Part 1: Unbelievable. I had it immediately (leaderboard position), but forgot to add 4 to
        # my answer. Once I figured that out, I added 4 to 1096 to get 2000. Spent another 8
        # minutes on that. Ended up in 5000th place, when I could have easily been 100th.
        print (c + 4)
        break

for c in range(0, len(signal)-14):
    if len(set(signal[c:c+14])) == 14:
        # Part 2: I need to learn that sometimes it just makes more sense to modify the previous
        # answer to get part 2 rather than right a whole extra solution
        print (c + 14)
        break