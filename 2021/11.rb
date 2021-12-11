require 'set'
lines = File.open("11.txt").readlines.map(&:strip)
#Pad the array
grid = [["*","*","*","*","*","*","*","*","*","*","*","*"]]
lines.each {|line| grid << ["*"] + line.chars.map(&:to_i) + ["*"]}
grid << ["*","*","*","*","*","*","*","*","*","*","*","*"]

flashes = 0
_ = 0
while 1
	_ += 1
	flash_change = 0
	flashed = Set[]
	#Increment everything by 1
	(1..10).each do |r|
		(1..10).each do |c|
			grid[r][c] += 1
		end
	end
	to_flash = []
	#Add items that are already at 10 to be flashed
	(1..10).each do |r|
		(1..10).each do |c|
			to_flash << [r, c] if grid[r][c] > 9
		end
	end
	#Flash simultaneously
	while !to_flash.empty?
		r, c = to_flash.pop
		grid[r][c] = 0
		flashed << [r, c]
		flash_change += 1
		(-1..1).each do |i|
			(-1..1).each do |j|
				if grid[r+i][c+j] != "*" and !flashed.include?([r+i, c+j])
					grid[r+i][c+j] += 1 
					to_flash << [r+i, c+j] if !to_flash.include? [r+i, c+j] and grid[r+i][c+j] > 9
				end
			end
		end
	end
	abort(_.to_s) if flash_change == 100 #Added abort after the fact
	flashes += flash_change
	p flashes if _ == 100
end

=begin part1
	Unbelievable. Checking grid[r][c] instead of [r, c] kept me out for 25 minutes. Another 20 on 
	not checking if an item was already in to_flash. So much wasted potential man
=end
=begin part2
	Actually easy lol. Had some weird printing and a 1 off error because I tried to use one-liners,
	but I knew how to do it instantly. Didn't require a lot of modification.
=end