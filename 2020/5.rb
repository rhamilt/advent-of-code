# RETARD! RECOGNIZE BINARY!

lines = File.open("5.txt").readlines.map(&:strip)#.map(&:to_i)
seats = []
lines.each do |line|
	currRange = (0..127).to_a
	7.times do |i|
		line[i] == "F" ? currRange = currRange[0..currRange.size/2]: currRange = currRange[currRange.size/2..]
	end
	row = currRange[0]
	currRange = (0..7).to_a
	3.times do |i|
		line[i+7] == "L" ? currRange = currRange[0..currRange.size/2]: currRange = currRange[currRange.size/2..]
	end
	col = currRange[0]
	seats << [row, col]
end

seatIDs = seats.map {|seat| seat[0] * 8 + seat[1]}.sort
puts seatIDs.max
(0..seatIDs.size-2).each do |i|
	if seatIDs[i+1] - 2 == seatIDs[i]
		puts seatIDs[i] + 1
	end
end

######################SAME BUT BETTER######################
ids = lines.map{|line| line.tr("FBLR","0101").to_i(2)}.sort
puts ids[-1]
(0..ids.size-2).each {|i| puts ids[i] + 1 if ids[i+1] - 2 == ids[i]}