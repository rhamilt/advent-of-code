lines = File.open("5.txt").readlines.map(&:strip)#.map(&:to_i)

p2 = false
2.times do |_|
	grid = Hash.new{0}
	lines.each do |line|
		m = line.match /(\d+),(\d+) -> (\d+),(\d+)/
		x1, y1, x2, y2 = m[1].to_i, m[2].to_i, m[3].to_i, m[4].to_i
		if x1 == x2
			if y1 > y2
				tmp = y1
				y1 = y2
				y2 = tmp
			end
			(y1..y2).each do |y|
				grid[[x1, y]] += 1
			end
		elsif y1 == y2
			if x1 > x2
				tmp = x1
				x1 = x2
				x2 = tmp
			end
			(x1..x2).each do |x|
				grid[[x, y1]] += 1
			end
		elsif p2
			#This ternary checks if x1 is less than x2
			#If it is, I start from (x1, y1)
			#If it's not, I start from (x2, y2)
			x, y, xNot, yNot = x1 < x2 ? [x1, y1, x2, y2] : [x2, y2, x1, y1]
			#Checking the sign so we can change the direction we travel in for y
			ysign = (yNot - y)/((yNot - y).abs)
			idx = 0
			while x + idx <= xNot
				grid[[x + idx, y + (idx * ysign)]] += 1
				idx += 1
			end	
		end
	end
	p2 = !p2
	p grid.select {|point, freq| freq > 1}.length
end

=begin part 1
	Not sure if there's really a better solution, I just took too long to type it out and had a couple bugs.
	a) Didn't realize that x1 could be greater than x2. b) Didn't realize I was supposed to skip some of the
	inputs for part 1 (even though it said that)
=end
=begin part 2
	Foolishly tried to set up 4 cases for all the different x1 < x2 y1 > y2 type deals and it turned out to be 
	a mess. Eventually figured out that if we start at x1 we have to start at y1 as well, and then it's just 
	a matter of figuring where to start, and how the y is going to change. Not too bad, but I would have liked
	to have intuited that faster :(. Very demoralizing past couple of days. 
=end
