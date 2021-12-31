require "set"
X, Y, Z = 0, 1, 2

lines = File.open("19.txt").read
scannerStrings = lines.split("\r\n\r\n")
scanners = Hash.new { |scanners, key| scanners[key] = [] }
scannerStrings.each_index do |scanner|
	scannerStrings[scanner].split("\n")[1..].each do |point|
		scanners[scanner] << point.split(",").map(&:to_i)
	end
end

distances = Hash.new { |distances, key| distances[key] = Set[] }
scanners.each do |scanner, beacons|
	beacons.each do |beacon1|
		beacons.each do |beacon2|
			if beacon1 != beacon2
				xdiff = (beacon1[X] - beacon2[X]).abs
				ydiff = (beacon1[Y] - beacon2[Y]).abs
				zdiff = (beacon1[Z] - beacon2[Z]).abs
				distances[scanner] << [beacon1, beacon2, Set[xdiff, ydiff, zdiff]]
			end
		end
	end
	(0...beacons.length-1).each do |idx|
	end
end

scannerDists = {}
common = Hash.new { |common, key| common[key] = Set[] }
distances.each do |scanner1, distances1|
	p "scanner1 #{scanner1}"
	distances.each do |scanner2, distances2|
		#p "scanner2 #{scanner2}"
		break if scanner1 == scanner2
		distances1.each do |dd1|
			distances2.each do |dd2|
				#dd1, dd2 = distances1[idx1], distances2[idx2]
				beacon1_1, beacon1_2, distance1 = dd1[0], dd1[1], dd1[2]
				beacon2_1, beacon2_2, distance2 = dd2[0], dd2[1], dd2[2]
				'''
				p beacon1_1, beacon1_2
				p distance1
				p beacon2_1, beacon2_2
				p distance2
				'''
				if distance1 == distance2
					scannerDists[[scanner1, scanner2]] = beacon1_1
					#common[Set[scanner1, scanner2]] << [scanner1] + beacon1_1 << [scanner2] + beacon2_1
					scanners[scanner2] -= [beacon2_1]
					scanners[scanner2] -= [beacon2_2]
					#p scanners
				end
			end
		end
		#puts common[[scanner1, scanner2]].length
		#gets.chomp
	end
end
p scanners
#p common[Set[0, 1]]
#common.select! {|scanners, beacons| beacons.length == 12}
#p common
beacons = []
scanners.each do |scanner, scannerBeacons|
	beacons += scannerBeacons
end
p beacons.length
dists = []
