require 'set'
DIRS = {"U" => [0, 1], "D" => [0, -1], "L" => [-1, 0], "R" => [1, 0]}
manhattan = Proc.new {|x| x[0].abs + x[1].abs}

def placeWire(instrucs, path1={})
	path = Hash.new
	curr = [0, 0]
	steps = 1
	common = []
	commonSteps = []
	instrucs.each do |instruc|
		instruc[1..].to_i.times do
			curr = [curr[0] + DIRS[instruc[0]][0], curr[1] + DIRS[instruc[0]][1]]
			path[curr.clone] = steps
			if path1.has_key?(curr)
				commonSteps << [path1[curr.clone], steps]
				common << curr.clone
			end
			steps += 1
		end
	end
	yield common
	yield commonSteps
	return path
end

lines = File.readlines("day3.txt")
lines.map! {|x| x.split(",").map {|y| y.strip}}

path1 = placeWire(lines[0]) {}
path2 = placeWire(lines[1], path1) {|common| puts common.map(&manhattan).sort[0]}