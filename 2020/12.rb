DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]].freeze
ROTATIONS = [
	lambda {|x, y| return [y, -x]},
	lambda {|x, y| return [-x, -y]}, 
	lambda {|x, y| return [-y, x]}].freeze

def rotate(waypoint, dir, mag)
	case mag
	when "90"
		if dir == "R"
			temp = ROTATIONS[0].call(waypoint[0], waypoint[1])
		else
			temp = ROTATIONS[2].call(waypoint[0], waypoint[1])
		end
	when "270"
		if dir == "R"
			temp = ROTATIONS[2].call(waypoint[0], waypoint[1])
		else
			temp = ROTATIONS[0].call(waypoint[0], waypoint[1])
		end
	else
		temp = ROTATIONS[1].call(waypoint[0], waypoint[1])
	end
	return temp
end

lines = File.open("12.txt").read.split("\n")
p2 = false
2.times do |_|
	pos, currDir, waypoint = [0, 0], 1, [10, 1]
	lines.each do |line|
		instruc, mag = line.match(/(\w)(\d+)/).captures
		if "NESW".include? instruc
			dir = DIRS["NESW".index(instruc)]
			mag.to_i.times do |i|
				if !p2
					pos[0] += dir[0]
					pos[1] += dir[1]
				else
					waypoint[0] += dir[0]
					waypoint[1] += dir[1]
				end
			end
		else
			case instruc
			when "F"
				mag.to_i.times do |i|
					if !p2
						pos[0] += DIRS[currDir][0]
						pos[1] += DIRS[currDir][1]
					else
						pos[0] += waypoint[0]
						pos[1] += waypoint[1]
					end
				end
			when "L"
				if !p2
					currDir = (currDir - (mag.to_i/90)) % DIRS.size
				else
					waypoint = rotate(waypoint, "L", mag)
				end
			else
				if !p2
					currDir = (currDir + (mag.to_i/90)) % DIRS.size
				else
					waypoint = rotate(waypoint, "R", mag)
				end
			end
		end
	end
	p2 = !p2
	puts pos.map {|x| x.abs}.sum
end