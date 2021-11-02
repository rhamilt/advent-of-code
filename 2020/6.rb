lines = File.open("6.txt").readlines.map(&:strip)#.map(&:to_i)

cnt1, cnt2 = 0, 0
curr = ''
lines.each do |line|
	if line == ""
		cnt1 += curr.split.join.chars.uniq.size
		cnt2 += curr.split.map(&:chars).inject(:&).size
		curr = ''
	else
		curr << ' ' + line.strip
	end
end
puts cnt1
puts cnt2

lines2 = File.open("6.txt").read.split("\n\n")
p lines2.map{|x| x.split.join.chars.uniq.size}.sum
p lines2.map{|x| x.split.map{|x| x.chars}.reduce(:&).size}.sum