require 'set'
lines = File.open("10.txt").readlines.map(&:strip)#.map(&:to_i)

error = 0
opening = "([{<"
closing = ")]}>"
points1 = {")":3,"]":57,"}":1197,">":25137}
points2 = {"(":1,"[":2,"{":3,"<":4}
totals = []
lines.each do |line|
	stack = []
	line.chars.each do |char|
		if opening.include? char
			stack << char
		else 
			if stack[-1] == opening[closing.index(char)]
				stack.pop
			else
				error += points1[char.intern] #intern because they're stored as symbols
				stack = []
				break
			end
		end
	end
	if !stack.empty?
		total = 0
		stack.reverse.each do |char|
			total *= 5
			total += points2[char.intern] #intern because they're stored as symbols
		end
		totals << total
	end
end

=begin part 1
	So sad that I knew instantly how to do this problem. Slowed down by typographical errors
	and the fact that I missed the difference between corrupted and incomplete. = vs == is a killer
=end
p error

=begin part 2
	Did this part pretty quickly, just forgot to sort the totals before I took the middle so that
	cost me a minute. Overall happy with my solution
=end
p totals.sort[totals.length/2]