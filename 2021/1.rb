lines = File.open("1.txt").readlines.map(&:strip).map(&:to_i)
p1 = 0
p2 = 0
prevVal = 100000
prevSum = 100000
window = []

(0...lines.length).each do |each|
	p1 += 1 if lines[each] > prevVal
	prevVal = lines[each]
	window = lines[each...each+3]
	p2 += 1 if window.sum > prevSum
	prevSum = window.sum
end

=begin part 1
	Did this very quickly, LEADERBOARD 76 BABEEE
=end
p p1

=begin part 2
	I mega choked on this part. Got rejected two times. Stupid .. vs ... for list slice.
=end
p p2 