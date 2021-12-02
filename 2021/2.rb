lines = File.open("2.txt").readlines.map(&:strip)#.map(&:to_i)

horiz = 0
vert = 0
aim = 0
horiz2 = 0
vert2 = 0

(0...lines.length).each do |i|
	direc, amount = lines[i].split
	horiz += amount.to_i if direc == "forward"
	vert += amount.to_i if direc == "down"
	vert -= amount.to_i if direc == "up"
	aim += amount.to_i if direc == "down"
	aim -= amount.to_i if direc == "up"
	horiz2 += amount.to_i if direc == "forward"
	vert2 += amount.to_i * aim if direc == "forward"
end

=begin part1
	Did it quickly, just not quick enough for leaderboard (#160) 1:48
=end
p vert * horiz

=begin part2
	No major bugs, but frankly took too long to type and forgot what the differene
	between aim, depth, distance traveled were.
=end
p vert2 * horiz2