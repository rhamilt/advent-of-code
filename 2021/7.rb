nums = File.open("7.txt").read.split(",").map(&:strip).map(&:to_i)

minFuel = Float::INFINITY #Found this online (used 100000000 at comp time lol)
minFuel2 = Float::INFINITY
nums.max.times do |i|
	minFuel = [minFuel, nums.map{ |x| (x-i).abs }.sum].min
	minFuel2 = [minFuel2, nums.map{|x| (1..(x-i).abs).sum }.sum].min
end

=begin part 1
	Did it pretty easily, took me a couple minutes I think but no major hiccups
=end
p minFuel
=begin part 2
	Pretty proud of myself for this one, did it quickly as well and knew what to do.
	Accidentally tried to use .inject(:*) instead of sum (no reason whatsoever). Also forgot
	to take absolute value of x-i even though I did it in the first part
=end
p minFuel2