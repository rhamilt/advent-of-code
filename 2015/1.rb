line = File.open("1.txt").read

total = 0
index = 1
wasPos = true
line.chars do |paren|
    paren == "(" ? total += 1 : total -= 1
    wasPos = false if total < 0 and wasPos
    index += 1 if wasPos
end
=begin part 1
    Straight forward. Loop through all parens, print result
=end
p total
=begin part 2
    I didn't really bother to read the second part and just assumed
    it was asking to find the place that we first get to twice. I should 
    have read more carefully. Not hard once I did
=end
p index
