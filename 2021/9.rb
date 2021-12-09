require 'set'
lines = File.open("9.txt").readlines.map(&:strip)#.map(&:to_i)
grid = []
lines.each {|line| grid <<  line.chars.map(&:to_i)}

low_points = []
total = 0
(0..grid.length-1).each do |r|
	(0..grid[0].length-1).each do |c|
		low = true
		low = false if r-1 >= 0 and grid[r-1][c] <= grid[r][c]
		low = false if r+1 < grid.length and grid[r+1][c] <= grid[r][c]
		low = false if c-1 >= 0 and grid[r][c-1] <= grid[r][c]
		low = false if c+1 < grid[0].length and grid[r][c+1] <= grid[r][c]
		low_points << [r, c] if low
	end
end

=begin part 1
	Wasn't actually hard to do, just had a crazy amount of bounds errors. You wouldn't
	believe the time I spent on various bounds changes (about 12 minutes)
=end
p low_points.map {|point| grid[point[0]][point[1]]+1}.sum

basins = []
low_points.each do |low_point|
	basin = Set[]
	r,c = low_point[0], low_point[1]
	q = [[r, c]]
	q << [r-1, c] if r-1 >= 0
	q << [r+1, c] if r+1 < grid.length
	q << [r, c-1] if c-1 >= 0
	q << [r, c+1] if c+1 < grid[0].length
	while !q.empty?
		point = q.shift
		r,c = point[0], point[1]
		if grid[r][c] != 9
			basin << [r, c]
			q << [r-1, c] if r-1 >= 0 and !basin.include? [r-1, c]
			q << [r+1, c] if r+1 < grid.length and !basin.include? [r+1, c]
			q << [r, c-1] if c-1 >= 0 and !basin.include? [r, c-1]
			q << [r, c+1] if c+1 < grid[0].length and !basin.include? [r, c+1]
		end
	end
	basins << basin
end

=begin part 2
	Crazily I did this part first try. Only hiccup was I accidentally summed instead of mult.
	Also briefly forgot to check basin include for inf. loop but fixed immediately. Happy
	with how I did this one.
=end
p basins.sort_by {|s| s.length}[-3..].map{|s| s.length}.inject(:*)
#Proud of this little one liner to take multiplied lengths of top 3