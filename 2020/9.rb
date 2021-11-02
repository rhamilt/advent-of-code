lines = open("9.txt").read.split("\n").map(&:to_i)
curr = []
idx = 0
while true
	if idx >= 25
		num = lines[idx]
		works = curr.combination(2).to_a.select {|x| x.sum == num}.size() >= 1
		break if !works
		curr.shift
		curr << num
	else
		curr << lines[idx]
	end
	idx += 1
end
puts num

idx2 = 0
sum = 0
len = 0
while true
	while sum < num
		sum += lines[idx2 + len]
		len += 1
	end
	break if sum == num
	sum -= lines[idx2]
	idx2 += 1
	len -= 1
end
temp = lines[idx2..idx2 + len - 1].sort
puts temp[0] + temp[-1]