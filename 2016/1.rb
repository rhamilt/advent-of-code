require "Set"
lines = File.open("1.txt").read.split(",").map(&:strip)#.map(&:to_i)
location = [0, 0]
direc = 0
direcs = [[0, 1],[1, 0],[0, -1],[-1, 0]]
seen = Set[[0, 0]]
p2 = false #So we only print most recently seen one time
lines.each do |line|
	line[0] == "R" ? direc = (direc + 1) % 4 : direc = (direc - 1) % 4
	(0...line[1..].to_i).each do |i|
		location[0] += direcs[direc][0]
		location[1] += direcs[direc][1]
		if seen.include? location and !p2
			puts "seen: #{location.map(&:abs).sum}"
			p2 = true
		else
			seen << location
		end
	end
end
=begin part 1 
Took me an embarrassingly long time. I wish I had realized that it was a rotation and not just
going left and right LOL. I should probably figure out a better way to handle a rotation.
Seems a bit hard for day 1.
=end
p location.map(&:abs).sum
=begin part 2
Took me an embarrassingly long time. Kind of annoying that it's every place you passed over,
not just the ones you landed on. Didn't help that I had to restructure my code.
=end