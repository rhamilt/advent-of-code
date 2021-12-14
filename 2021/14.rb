str_start, instrucs = File.open("14.txt").read.split("\n\n")
replacements = {}
instrucs.split("\n").each do |instruc|
	start, replace = instruc.split " -> "
	replacements[start] = replace
end

str = str_start
10.times do
	newStr = ""
	(0...str.length).each do |idx|
		newStr << str[idx]
		break if idx == str.length-1
		newStr << replacements[str[idx]+str[idx+1]]
	end
	str = newStr
end

freqs = str.chars.tally.values #LOL goes hard
=begin part 1
	Man I just had some bugs. Originally forgot to sort the freqs, also was not
	adding very last character. Took longer than it should have, but I knew how to do it.
=end
p (freqs.max - freqs.min)

str = str_start
patterns, letters = Hash.new(0), Hash.new(0)
(0...str.length).each do |idx|
	letters[str[idx]] += 1
	break if idx == str.length-1
	patterns[str[idx]+str[idx+1]] += 1
end
40.times do
	newPatterns = Hash.new(0)
	patterns.each do |pattern, freq|
		newPattern1 = pattern[0] + replacements[pattern]
		newPattern2 = replacements[pattern] + pattern[1]
		letters[replacements[pattern]] += freq
		newPatterns[newPattern1] += freq
		newPatterns[newPattern2] += freq
	end
	patterns = newPatterns
end

freqs = letters.values
=begin part 2
	Sad because I actually figured out the clever fast way to do this pretty quickly.
	Just had trouble counting the frequency of the letters once I figured out how to do it,
	but eventually I figured it out. Also was resetting patterns freqeuncy dict in each 
	iteration of the for loop (for some unknown reason)
=end
p (freqs.max - freqs.min)