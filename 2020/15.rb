def game(nums, n)
	spoken, prev = Hash.new { |hash, key| hash[key] = [] }, nil
	n.times do |i|
		if i < nums.size
			spoken[nums[i]] << i
			prev = nums[i]
		else
			if spoken[prev].size == 1
				spoken[0] << i
				prev = 0
			else
				diff = spoken[prev][-1] - spoken[prev][-2]
				spoken[diff] << i
				prev = diff
			end
		end
	end
	puts prev
end

nums = File.open("15.txt").read.split(",").map(&:to_i)
game(nums, 2020)
game(nums, 30000000)