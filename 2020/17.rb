DXYZ = [-1, 0, 1]

def starting3(grid)
	space3 = Hash.new { |hash, key| hash[key] = 0}
	grid.size.times do |r|
		grid.size.times do |c|
			space3[[r, c, 0]] = 1 if grid[r][c] == "#"
		end
	end
	return space3
end

def starting4(grid)
	space4 = Hash.new { |hash, key| hash[key] = 0}
	grid.size.times do |r|
		grid.size.times do |c|
			space4[[r, c, 0, 0]] = 1 if grid[r][c] == "#"
		end
	end
	return space4
end

def near3(coord)
	nearby = []
	27.times do |i|
		dx, dy, dz = [DXYZ[i%3], DXYZ[i/3%3], DXYZ[i/9]]
		next if [dx, dy, dz] == [0, 0, 0]
		nearby << [coord[0] + dx, coord[1] + dy, coord[2] + dz]
	end
	return nearby
end

def near4(coord)
	nearby = []
	81.times do |i|
		dx, dy, dz, dw = [DXYZ[i%3], DXYZ[i/3%3], DXYZ[i/9%3], DXYZ[i/27]]
		next if [dx, dy, dz, dw] == [0, 0, 0, 0]
		nearby << [coord[0] + dx, coord[1] + dy, coord[2] + dz, coord[3] + dw]
	end
	return nearby
end

grid = File.open("17.txt").read.split("\n")
space3 = starting3(grid)
space4 = starting4(grid)

6.times do |x|
	temp3 = Hash.new { |hash, key| hash[key] = 0}
	temp4 = Hash.new { |hash, key| hash[key] = 0}
	frontier = space3.keys + space4.keys
	seen = []
	while frontier.size > 0
		curr = frontier.shift
		next if seen.include? curr
		seen << curr
		if curr.size == 3
			nearby = near3(curr)
			frontier += nearby if space3[curr] == 1
			count = nearby.map {|coord| space3[coord]}.sum
			if space3[curr] == 1
				temp3[curr] = 1 if count == 2 || count == 3
			else
				temp3[curr] = 1 if count == 3
			end
		else
			nearby = near4(curr)
			frontier += nearby if space4[curr] == 1
			count = nearby.map {|coord| space4[coord]}.sum
			if space4[curr] == 1
				temp4[curr] = 1 if count == 2 || count == 3
			else
				temp4[curr] = 1 if count == 3
			end
		end
	end
	space3 = temp3
	space4 = temp4
end

p space3.size
p space4.keys.map {|k| k[3] == 0 ? 1: 0}.sum