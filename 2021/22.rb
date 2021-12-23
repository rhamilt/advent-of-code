#Checks whether 2 prisms are overlapping
def overlap(p1, p2) #Prism1, Prism2
	x = ((p1[0] <= p2[0] and p1[1] > p2[0]) or (p2[0] <= p1[0] and p2[1] > p1[0]))
	y = ((p1[2] <= p2[2] and p1[3] > p2[2]) or (p2[2] <= p1[2] and p2[3] > p1[2]))
	z = ((p1[4] <= p2[4] and p1[5] > p2[4]) or (p2[4] <= p1[4] and p2[5] > p1[4]))
	return (x and y and z)
end

#Checks if prism1 fully contains prism2
#Used to check if a sub block is in a give block
def contains(p1, p2) #Prism1, prism2
	return (p1[0]<=p2[0] and p2[1]<=p1[1] and p1[2]<=p2[2] and p2[3]<=p1[3] and p1[4]<=p2[4] and p2[5]<=p1[5])
end

lines = File.open("22.txt").readlines.map(&:strip)

reactor = Hash.new(0)

lines.each do |line|
	m = line.match(/(on|off) x=(-?\d+..-?\d+),y=(-?\d+..-?\d+),z=(-?\d+..-?\d+)/)
	status, xRange, yRange, zRange = (m[1]=="on" ? 1 : 0), eval(m[2]), eval(m[3]), eval(m[4])
	xRange.each do |x|
		break if x.abs > 50
		yRange.each do |y|
			break if y.abs > 50
			zRange.each do |z|
				break if z.abs > 50
				reactor[[x,y,z]] = status
			end
		end
	end
end

=begin part 1
	Happy with how I did this, considering I came first in our private leaderboard. About 10 minutes, most
	of the hiccups came from the limiting to -50..50: I didn't realize that we just exit if one of them is
	any single point is not in that range. Of course this is the naive way, but not bad overall I think.
=end
p reactor.values.sum

regions = []

lines.each do |line|
	m = line.match(/(on|off) x=(-?\d+..-?\d+),y=(-?\d+..-?\d+),z=(-?\d+..-?\d+)/)
	status, xRange, yRange, zRange = m[1]=="on", eval(m[2]), eval(m[3]), eval(m[4])
	#Region arrays are split up as: [xmin, xmax, ymin, ymax, zmin, zmax]
	#Basically, an array of distinct values instead of [xRange, yRange, zRange]
	#Must add 1 to max values in order to handle the fact that 10..10 is 1 block, not 0
	cRegion = [xRange.min, xRange.max+1, yRange.min, yRange.max+1, zRange.min, zRange.max+1]
	newRegions = []
	regions.each do |region|
		if overlap(cRegion, region) #Check if our regions overlap
			#the _Points arrays are ways of getting around different orientations of blocks
			#This way, we have a convenient point to divide our 27 subregions of the two 
			#regions we're examining.
			#Each array is the "fencepost" values for that dimension for the two regions, in order
			xPoints = (cRegion[..1] + region[..1]).sort
			yPoints = (cRegion[2..3] + region[2..3]).sort
			zPoints = (cRegion[4..5] + region[4..5]).sort
			#Given xPoints [0,1,2,3]
			#These x loop will give us [0,1], [1,2], [2,3]
			3.times do |x|
				3.times do |y|
					3.times do |z|
						newRegion = xPoints[x..x+1] + yPoints[y..y+1] + zPoints[z..z+1]
						#If our new subregion is in our old region and not in our new one,
						#We add it back to our regions. Otherwise, it might be outside of both
						#(don't add it at all), or part of our region we're examining, which
						#is handled later.
						if contains(region, newRegion) and !contains(cRegion, newRegion)
							newRegions << newRegion
						end
					end
				end
			end
		else #If our region doesn't intersect the new region we're examining, add it back immediately
			newRegions << region
		end
	end
	newRegions << cRegion if status #Add the region we're examining if we're turning it on, leave it if not
	regions = newRegions.clone
end

=begin part 2
	Overall very happy with how this solution ended up coming out. Started with this idea of splitting
	up old regions, but it went through many different changes before arriving here. Decent amount of time
	lost on the fact that "if 0" is true :|. Probably would have been easier if I'd developed a prism object.
	Also lost some time in bounds of regions: 10..10 is 1 block, but 10-10 is 0, so I had to account for that
	somewhere.
=end
p regions.map {|r| ((r[1]-r[0])*(r[3]-r[2])*(r[5]-r[4]))}.sum
#Only using r to save space, "region" would be more descriptive