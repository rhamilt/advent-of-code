lines = File.open("6.txt").read.split(",").map(&:strip).map(&:to_i)

fishes = lines.clone
80.times do |_|
	to_add = []
	fishes.each_index do |fish|
		if fishes[fish] == 0
			to_add << 8
			fishes[fish] = 6
		else
			fishes[fish] -= 1
		end
	end
	fishes += to_add
end

=begin part 1
	Prety standard way to do everything I think, I accidentally did == -1 instead of == 0
	and that caused me some trouble. Just a stupid mistake but still relatively quick.
=end
p fishes.length

day = 0
ageFreq = [0, 0, 0, 0, 0, 0, 0, 0, 0] #Because there are 9 possible ages (0-8)
lines.each {|fish| ageFreq[fish] += 1}

256.times do |_|
	dyingFishCount = ageFreq.shift #I know they aren't dying, just being reborn
	ageFreq += [dyingFishCount]
	ageFreq[6] += dyingFishCount
end

=begin part 2
	Took me a while to figure out an efficient method. Eventually after trying to draw out a bunch
	of trees on paper (LOL), I finally realized that it's a matter of keeping track of how many
	there are at each age, and then adding the reborn ones back onto the age 6, age 8 ones.
=end
p ageFreq.sum