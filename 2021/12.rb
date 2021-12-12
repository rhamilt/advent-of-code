require 'set'
lines = File.open("12.txt").readlines.map(&:strip)#.map(&:to_i)

bigs = Set[]
smalls = Set[]
connections = Hash.new { |connections, key| connections[key] = Set[] }
lines.each do |line|
	c1, c2 = line.split("-")
	c1 == c1.upcase ? bigs << c1 : smalls << c1
	c2 == c2.upcase ? bigs << c2 : smalls << c2
	connections[c1] << c2
	connections[c2] << c1
end

paths = Set[]
paths2 = Set[]
frontier = [["start"]]
while !frontier.empty?
	path = frontier.pop
	if path[-1] == "end"
		paths2 << path
		smallCounts = path.tally.select {|cave, freq| smalls.include? cave}
		paths << path if smallCounts.values.sum <= smallCounts.length
		next
	end
	possibles = connections[path[-1]]
	possibles.each do |possible|
		newPath = path + [possible]
		next if newPath.count("start") > 1
		smallCounts = newPath.tally.select {|cave, freq| smalls.include? cave}
		next if smallCounts.values.sum > smallCounts.length + 1
		frontier << newPath if !frontier.include? newPath
	end
end	

=begin part 1
	I actually did quite well on this part. DFS done first try with no hiccups. Got 311 on part 1. Is this
	a sign because I have my CSE 311 final in 2 days?
=end
p paths.length

=begin part 2
	Much more annoying. Tried to go too complicated at first (although I was still correct), but the real
	killer was the fact that I FORGOT TO REMOVE MY PART 1 CODE! Somehow took me forever to find this. Why
	do I always do this :'(
=end
p paths2.length