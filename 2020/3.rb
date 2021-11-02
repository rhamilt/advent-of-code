lines = File.open("3.txt").readlines.map(&:strip)
count_overall = 1
(1..7).step(2) do |step|
	count = 0
	idx = 0
	lines.each do |x|
		count += 1 if x[idx % x.size] == "#"
		idx += step
	end
	puts count if step == 3
	count_overall *= count
end

count = 0
idx = 0
(0..lines.size).step(2) do |x|
	count += 1 if lines[x][idx % lines[x].size] == "#"
	idx += 1
end
count_overall *= count

puts count_overall