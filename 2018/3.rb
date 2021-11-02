lines = File.open("3.txt").readlines.map(&:strip)

grid = {}
grid.default = []
ids = []
lines.each do |line|
	id, startx, starty, totx, toty = line.match(/^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$/).captures.map(&:to_i)
	ids << id
	for x in (startx...(startx+totx))
		for y in (starty...(starty+toty))
			combine = proc {|x,y| (x+y)*(x+y+1)+y}
			grid[combine.(x,y)] = grid[combine.(x,y)] + [id] #WILD SHIT
		end
	end
end
overlapping = grid.select {|k, v| v.length > 1 }
puts overlapping.length

overlapping.keys.each do |key|
	overlapping[key].each do |id|
		ids.delete(id) if ids.include? id
	end
end
p ids[0]