require "set"
coordList, instrucs = File.open("13.txt").read.split("\n\n").map(&:strip)
=begin Interesting behavior explanation
	In testing this, I found that on the command line this doesn't work because of 
	carriage returns in the input. Instead, I have to split \n\r. However, that doesn't
	work then when I run it in sublime. Interesting thing that might be related to
	the version of ruby that I'm running?
=end

grid = Set[]
coordList.split.map(&:strip).each do |coord|
	x, y = coord.split(",").map(&:to_i)
	grid << [x, y]
end

count = 0
instrucs.split("\n").map(&:strip).each do |instruc|
	m = instruc.match /(x|y)=(\d+)/
	direc, line = m[1], m[2].to_i
	newGrid = Set[]
	grid.each do |point|
		idx = (direc == "y" ? 1 : 0)
		break if point[idx] == line
		newPoint = point
		newPoint[idx] = line - (point[idx]-line) if point[idx] > line
		newGrid << newPoint
	end
	grid = newGrid
	p grid.length if count == 0
	count += 1
end
=begin part 1
	Again I'm just a relatively slow typer, but I got it right first try and came 752.
	Obviously would have liked to do better, but at least I didn't have to debug
=end

#instantiate
gridLayout = []
6.times do |i| #These values are the exact size of the output did not do this in comp
	row = []
	39.times { row << "." }
	gridLayout << row
end
#fill array with points
grid.each { |point| gridLayout[point[1]][point[0]] = "#" }
#print
gridLayout.each { |row| puts row.join} #HZLEHJRK is the output
=begin part 2
	Kevin pointed out that you should just go through possible points and print a dot
	when there is a dot. Silly of me to actually make a grid like I did. Narrowly missed
	top 1000 on this one
=end