require 'set'
lines = File.open('2.txt').readlines.map(&:strip)

twos = 0
threes = 0
lines.each do |line|
	freqs = Hash.new(0)
	line.each_char{|char| freqs[char] += 1}
	twos += 1 if freqs.values.include? 2
	threes += 1 if freqs.values.include? 3
end
puts twos * threes

lines.each_with_index do |line, i|
	for j in (i+1...lines.length)
		union = ''
		for char in (0...line.length)
			union << line[char] if line[char] == lines[j][char]
		end
		union.length == line.length-1 ? (puts union; exit) : next
	end
end