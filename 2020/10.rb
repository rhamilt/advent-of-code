def counts(list)
	jolts = [0, 0, 0]
	(1..list.size-1).each do |item|
		diff = list[item] - list[item - 1]
		jolts[diff - 1] += 1
	end
	p jolts[0] * (jolts[2] + 1)
end

def possibles(spots, sorted, n)
	return 1 if n == 0
	return 0 if !sorted.include? n
	if (spots[n].nil?)
		spots[n] = 0
		(1..3).each do |x|
			spots[n] += possibles(spots, sorted, n - x) 
		end
	end
	return spots[n]
end

sorted = open("10.txt").read.split("\n").map(&:to_i).sort
counts([0] + sorted)
p possibles([], sorted, sorted[-1])