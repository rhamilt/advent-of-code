require 'set'
lines = File.open("8.txt").readlines.map(&:strip)#.map(&:to_i)

total = 0
lines.each do |line|
	matches = line.split[-4..]
	matches.each do |m|
		len = m.length
		total += 1 if len == 2 or len == 4 or len == 3 or len == 7
	end
end	
=begin part 1
	This part was not hard, but I spent too much time trying to figure out the whole problem.
	It didn't even end up paying off in the second half LOL.
=end
p total

total2 = 0
lines.each do |line|
	matches = line.split - ["|"]
	sigPatterns = matches[...10]
	output = matches[-4..]
	nums = {}
	sigPatterns.sort_by{|x| x.length}.each do |patternString|
		pattern = patternString.chars.to_set
		len = pattern.length
		case len
		when 2
			nums["1"] = pattern
		when 3
			nums["7"] = pattern
		when 4
			nums["4"] = pattern
		when 7
			nums["8"] = pattern
		when 5
			if nums["1"] & pattern == nums["1"]
				nums["3"] = pattern
			elsif (nums["4"] & pattern).length == 3
				nums["5"] = pattern
			else
				nums["2"] = pattern
			end
		when 6
			if (nums["1"] & pattern).length == 1
				nums["6"] = pattern
			elsif nums["3"] & pattern == nums["3"]
				nums["9"] = pattern
			else
				nums["0"] = pattern
			end
		end
	end
	subtotal = ""
	output.map(&:chars).each do |pattern|
		(0..9).each do |i|
			subtotal << i.to_s if nums[i.to_s] == pattern.to_set
		end
	end
	total2 += subtotal.to_i
end	


=begin part 2
	I didn't actually do this on the day of because I couldn't figure it out fast enough
	and had other stuff to do. Felt actually pretty simple the next day when I came back to it,
	but this problem was trickier than I would have liked it to be. 
=end
p total2
