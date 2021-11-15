polymer = File.open("5.txt").read

def react(polymer)
	newPoly = []
	polymer.split('').each do |char|
		newPoly[-1] == char.swapcase ? newPoly.pop : newPoly << char
	end
	return newPoly
end

=begin Part 1
Pretty simple to just go through the string and append things to an array, although
it took me longer than it should have.
=end
p react(polymer).length

newPolys = []
"abcdefghijklmnopqrstuvwxyz".split("").each do |unit|
	newPolys << react(polymer.gsub(unit, "").gsub(unit.upcase, ""))
end

=begin Part 2
For part 2, I just had to figure out the proper way to properly replace in ruby
After I tried a couple of different things, I found gsub which worked best.
=end
p newPolys.min_by{|poly| poly.length}.length