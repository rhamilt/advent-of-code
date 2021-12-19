def snailfishAdd(sum, snailfish)
	sf = "[" + sum + "," + snailfish + "]"
	idx = 0
	unchanged = false
	while !unchanged
		orig = sf.clone
		countBrackets = 0
		#Explode as many as possible 
		#Any possible explodes are done before splits for some reason (I wouldn't have mad the problem this way)
		while idx < sf.length
			if countBrackets == 5
				left, right = sf[idx..].match(/\d+,\d+/)[0].split(",")
				sf = sf[...idx-1] + sf[idx-1..].sub!(/\[#{left},#{right}\]/, "0")
				leftPortion, rightPortion = sf[..idx-2], sf[idx..]
				if leftPortion.match(/(.*)([0-9]+)/) #Have to have if in case there is no match
					#Have to do reversing to handle multi digit numbers
					newLeft = (leftPortion.reverse.match(/([0-9]+)/)[1].reverse.to_i + left.to_i).to_s.reverse
					leftPortion = leftPortion.reverse.sub(/([0-9]+)/, newLeft).reverse
				end
				if rightPortion.match(/(\d+)/)
					newRight = (rightPortion.match(/(\d+)/)[1].to_i + right.to_i).to_s
					rightPortion.sub!(/(\d+)/, newRight)
				end
				sf = leftPortion + "0" + rightPortion
				idx = 0
				countBrackets = 0
				next
			else
				countBrackets += 1 if sf[idx] == "["
				countBrackets -= 1 if sf[idx] == "]"
				idx += 1
			end
		end
		idx = 0
		#Now go back and find the first irregular number to be split
		while idx < sf.length
			if sf[idx].match(/[0-9]/) and sf[idx+1].match(/[0-9]/)
				value = (sf[idx] + sf[idx+1]).to_i
				left, right = value/2, (value/2.0).ceil
				sf.sub!(value.to_s, "[#{left},#{right}]")
				break
			end
			idx += 1
		end
		idx = 0
		unchanged = orig == sf
	end
	return sf
end

def magnitude (snailfish)
	return snailfish if snailfish.class == Integer
	return 3 * magnitude(snailfish[0]) + 2 * magnitude(snailfish[1])
end

=begin part 1
	What a doozy man. I estimate that I spent about 6 hours on this problem, two on day of.
	Once I figured out that I was doing string manipulation, it was a lot of long debugging
	witch gets.chomp to find all the edge cases. Frustrating that some of the inputs worked
	while others did not. This is some of the least interesting code to look at of all time.
=end
snailfishes = File.open("18.txt").readlines.map(&:strip)
p magnitude(eval(snailfishes.reduce { |sum, sf| snailfishAdd(sum, sf) }))


=begin part 2
	Very easy after part 1, but I don't think it was meant to be that difficult. Just
	used permutations and took the max of all possible perms. Runs slowly (9.9s) of course, but
	I could not care less ;)
=end	
snailfishes = File.open("18.txt").readlines.map(&:strip)
p snailfishes.permutation(2).map {|sf1, sf2| magnitude(eval(snailfishAdd(sf1, sf2)))}.max