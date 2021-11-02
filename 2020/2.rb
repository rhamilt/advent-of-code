lines = File.open("2.txt").readlines.map(&:strip)
count1 = 0
count2 = 0
lines.each do |x|
	min, max, char, pass = x.match(/(\d+)-(\d+) (\w): (\w+)/).captures
	count1 += 1 if pass.count(char) >= min.to_i && pass.count(char) <= max.to_i
	count2 += 1 if (pass[min.to_i-1] == char) ^ (pass[max.to_i-1] == char)
end
puts count1
puts count2