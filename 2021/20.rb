algo, imageRaw = File.open("20.txt").read.split("\n\n")
imageRaw = imageRaw.split

algo.gsub!(".", "0").gsub!("#", "1").gsub!("\n", "")
image = Hash.new(0)

imageRaw.length.times do |row| 
	imageRaw.length.times do |col|
		image[[row, col]] += 1 if imageRaw[row][col] == "#"
	end
end

50.times do |i|
	newImage = image.clone
	xVals = image.keys.map{|point| point[0]}
	yVals = image.keys.map{|point| point[1]}
	maxX, maxY = xVals.max, yVals.max
	minX, minY = xVals.min, yVals.min
	(minX-1..maxX+1).each do |r|
		(minY-1..maxY+1).each do |c|
			idx = ""
			(-1..1).each do |i|
				(-1..1).each do |j|
					idx += image[[r+i, c+j]].to_s
				end
			end
			newImage[[r,c]] = algo[idx.to_i(2)].to_i
		end
	end
=begin Hash new Default explanation
	This is only necessary if the input toggles on and off infinite bits.
	Toggling occurs when an index of 1111111111 results in a 0 and the index
	000000000 results in a 1, ie, the algo string is 1<510 bits>0. In the case
	where this is not true, you don't toggle
=end
	image = Hash.new((i+1)%2)
	newImage.each {|point, val| image[point] = val}
	p image.values.sum if i == 1
end

=begin part1 and 2
	Definitely did not bring my A game today. Thought and typed kind of slowly, but the real killer
	was the idea of the toggling bits on and off. After I figured out that there are infinite
	#s after an odd number of iterations with a toggling algorithm, I figured to reset the hash
	default value to 1 or 0 depending on the current iteration. This was easy, but I didn't realize
	that the example input DID NOT TOGGLE, and therefore the flipflopping default value was incorrect.
	After Kevin helped me realize this, I immediately submitted the correct answer. Kind of a bummer.
	Part 2 I just turned it on and waited the extra 30 seconds haha
=end
p image.values.sum