lines = File.readlines("day1.txt").map(&:to_i)
operation = Proc.new {|n| n / 3 - 2}
puts lines.map(&operation).sum #part 1

total = []
lines.each do |n|
	while n > 0
		n = operation.call(n)
		n > 0 ? total << n : total << 0
	end
end
puts total.sum #part 2