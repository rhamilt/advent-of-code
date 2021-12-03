lines = File.open("3.txt").readlines.map(&:strip)#.map(&:to_i)

total = Hash.new(0)
bits = lines[0].length
(0...bits).each do |idx| #For the 12 bits
	lines.each { |line| total[idx] += line[idx].to_i }
end
sum = ""
inv = ""
total.each {|idx, num| num > lines.length / 2 ? sum << "1" : sum << "0"}
total.each {|idx, num| num < lines.length / 2 ? inv << "1" : inv << "0"}
=begin part 1
	My roommates asked to watch and it really threw me off. I really like my solution
	but I just didn't get it quickly. Very disappointed in myself
=end
p (sum.to_i(2) * inv.to_i(2))

oxygenGenerator = ""
co2_scrubber = ""
oxy_lines = lines.clone
co2_lines = lines.clone
(0...bits).each do |idx|
	total = 0
	oxy_lines.each { |oxy_line| total += oxy_line[idx].to_i	}
	total < oxy_lines.length.to_f / 2 ? oxygenGenerator += "0" : oxygenGenerator += "1"
	oxy_lines = oxy_lines.select{|line| line[0..idx] == oxygenGenerator} #Selects only lines with curr. pattern
	total = 0
	co2_lines.each {|co2_line| total += co2_line[idx].to_i }
	if co2_lines.length == 1 #Must be done because single string will add 0 instead of whatever is in string
		co2_scrubber += total.to_s
	else
		total < co2_lines.length.to_f / 2 ? co2_scrubber += "1" : co2_scrubber += "0"
	end
	co2_lines = co2_lines.select{|line| line[0..idx] == co2_scrubber}
end

=begin part 2
	On top of my choke in part 1, I mega choked on this part. 30 extra minutes to solve
	after part 1. Took forever to read it too lol mad confusing.
=end
p (oxygenGenerator.to_i(2) * co2_scrubber.to_i(2))