m = File.open("17.txt").read.strip.match(/x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)/)
minX, maxX, minY, maxY = m[1].to_i, m[2].to_i, m[3].to_i, m[4].to_i

velos = []
maxYPos = -1.0/0.0 #Way to do negative inf (don't really need just think it's cool)
(0..maxX).each do |x|
	(minY..maxX+minY).each do |y| #I haven't really thought the math out, but it works :)
		position = [0, 0]
		velo = [x, y]
		maxYPosVelo = -1.0/0.0
		while position[0] <= maxX and position[1] >= minY
			position = [position[0] + velo[0], position[1] + velo[1]]
			maxYPosVelo = [maxYPosVelo, position[1]].max
			velo.map! {|_| _-1}
			velo[0] = [0, velo[0]].max
			if (minX..maxX).include? position[0] and (minY..maxY).include? position[1] 
				velos << [x, y]
				maxYPos = [maxYPos, maxYPosVelo].max
				break
			end
		end
	end
end

=begin part 1
	Pretty easy compared to the last two days, although it took me longer than I would of liked.
	The only major bug that kept me back was that I was accidentally letting the x velo be negative.	
=end
p maxYPos
=begin part 2
	Again this should have been easy considering how I did the first part with a list of all the
	acceptable velos. However, I must just have gotten lucky on p1 because I wasn't actually getting
	all the correct ones due to a >= vs > mistake.	
=end
p velos.length