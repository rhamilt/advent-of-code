grid = File.open("25.txt").readlines.map(&:strip).map(&:chars)
newGrid = []
step = 0

while true
	newGrid = []
	grid.each {|row| newGrid << row.join("").chars}
	grid.each_index do |r|
		grid[0].each_index do |c|
			if grid[r][c] == ">" and grid[r][(c+1)%grid[0].length] == "."
				newGrid[r][(c+1)%grid[0].length] = ">"
				newGrid[r][c] = "."
			end
		end
	end
	grid2 = []
	newGrid.each {|row| grid2 << row.join("").chars}
	grid2.each_index do |r|
		grid2[0].each_index do |c|
			if grid2[r][c] == "v" and grid2[(r+1)%grid.length][c] == "."
				newGrid[(r+1)%grid.length][c] = "v"
				newGrid[r][c] = "."
			end
		end
	end
	step += 1
	break if grid == newGrid
	grid = newGrid.clone
end

=begin part 1
	Was nobody going to tell me that clone only makes a shallow copy???? I guess it's been working
	for non-matrices, but this really screwed me over because i've been using it as a deep copy.
	It's ok though, just happy to have completed the challenges this year :)
=end
p step