require 'set'
def manDist(this, other)
	return (this[0] - other[0]).abs + (this[1] - other[1]).abs
end

def infinites(grid)
	infiniteList = Set[]
	for i in 0...500
		infiniteList << grid[[0, i]]
		infiniteList << grid[[i, 0]]
		infiniteList << grid[[349, i]]
		infiniteList << grid[[i, 349]]
	end
	return infiniteList
end
	
lines = File.open("6.txt").readlines.map(&:strip)
grid = {}
areaSizes = Hash.new(0)
coords = Set[]
lines.each do |stringCoord|
	coord = stringCoord.split(", ").map(&:to_i)
	coords << coord
end

#This next part is for optimization purposes
largestR = coords.max_by {|coord| coord[0]}[0]
largestC = coords.max_by {|coord| coord[1]}[1]
smallestR = coords.min_by {|coord| coord[0]}[0]
smallestC = coords.min_by {|coord| coord[1]}[1]

densest = []
for i in smallestR...largestR do
	for j in smallestC...largestC do
		tie = false
		totalDist = 0
		coords.each do |coord|
			grid[[i, j]] = [1000, 1000] if !grid.include? [i, j]
			dist = manDist([i, j], coord)
			totalDist += dist
			currMinDist = manDist([i, j], grid[[i, j]])
			if dist < currMinDist
				grid[[i, j]] = coord
				tie = false if tie
			elsif dist == currMinDist
				tie = true
			end
		end
 		areaSizes[grid[[i,j]]] += 1 if !tie
 		densest << [i, j] if totalDist < 10000
	end
end

=begin part 1
	This puzzle nearly killed me. So many little one off cases, I'm glad I finally got it over it.
	Overall, would not recommend!
=end
infinites(grid).each {|inf| areaSizes[inf] = -1}
p areaSizes.max_by {|coord, size| size}[1]
=begin part2
	Actually pretty easy, minor hiccup because I accidentally did densest + [i, j] instead of <<
=end
p densest.length