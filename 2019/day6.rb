def dfs(planet, orbiting)
	return planet == "COM" ? 0 : 1 + dfs(orbiting[planet], orbiting)
end

def search(orbiting, start, p2=false, seen={})
	count = 0
	myOrbits = {}
	planet = orbiting[start]
	while (p2 && !seen.key?(planet)) || (!p2 && planet != "COM")
		count += 1
		planet = orbiting[planet]
		myOrbits[planet] = count
	end
	return p2 ? count + seen[planet] : myOrbits
end

def searchForSanta(orbiting)
	myOrbits = search(orbiting, "YOU")
	return search(orbiting, "SAN", true, myOrbits)
end

lines = File.open("day6.txt").readlines.map(&:strip)
orbiting = Hash[lines.collect {|line| line.split(')').reverse}]
puts orbiting.map{|moon, planet| dfs(planet, orbiting)}.sum
puts searchForSanta(orbiting)