import time

def dfs(planet, planets):
	if planet == "COM":
		return 0
	else:
		return 1 + dfs(planets[planet], planets)

def planetDist(planet, orbiting, moons, seen, target="SAN"):
	if planet not in moons: 	  # if planet is end node
		return float('inf')
	elif target in moons[planet]: # if planet has SAN as moon
		return 0
	elif planet in seen:		  # if planet has been visited
		return float('inf')

	else:
		minimum = float('inf')
		for planetDown in moons[planet]:
			minimum = min(minimum, 1 + planetDist(planetDown, orbiting, moons, seen + [planet]))

		if planet != "COM":
			minimum = min(minimum, 1 + planetDist(orbiting[planet], orbiting, moons, seen + [planet]))

	return minimum #could return sooner but i think it looks simpler this way (only a .005s diff or smth)
	
	
def main():
	lines =  list(map(str.strip, open('day6.txt', 'r').readlines()))
	orbiting = {}
	moons = {}

	for line in lines:
		planet, moon = tuple(line.split(")"))
		orbiting[moon] = planet
		if planet not in moons:
			moons[planet] = []
		moons[planet].append(moon)

	sum1 = sum(dfs(planet, orbiting) for planet in orbiting)
	print (sum1) # part 1: did not take me very long, dfs'd through the 'tree'

	start = time.time()
	sum2 = planetDist(orbiting["YOU"], orbiting, moons, ["YOU"])
	print (time.time()-start)
	print (sum2) # part 2: i actually did this part crazy fast by my standards, kind of amazed that it worked

if __name__ == '__main__':
	main()