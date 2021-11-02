def addressFloat(starting)
	frontier = [starting]
	while frontier.size > 0
		address = frontier.pop
		if address.count("X") == 0
			yield address.sub("X", "0")
			yield address.sub("X", "1")
		else
			frontier << address.sub("X", "0")
			frontier << address.sub("X", "1")
		end
	end
end

def store(lines, p2=false)
	memory = !p2 ? {}: []
	lines.each do |line|
		mask, numsTemp = line.split("\n", 2)
		nums = numsTemp.split("\n")	
		nums.each do |eq|
			key, value = eq.match(/\[(\d+)\] = (\d+)/).captures
			toBin = "%036b" % value.to_i
			keyToBin = "%036b" % key.to_i
			if !p2
				memory[key.to_i] = ""
			else
				memory << ["", toBin]
			end
			(0..mask.size-1).each do |bit|
				if !p2
					memory[key.to_i] << (mask[bit] == "X" ? toBin[bit]: mask[bit])
				else
					memory[-1][0] << (mask[bit] != "0" ? mask[bit]: keyToBin[bit])
				end
			end
		end
	end
	return memory
end

lines = File.open("14.txt").read.split("mask = ").map(&:strip).drop(1)
memory = store(lines)
puts memory.values.map {|v| v.to_i(2)}.reduce {|v, sum| sum + v}
memory = {}
adresses = store(lines, true)
adresses.map {|address| addressFloat(address[0]) {|newAddress| memory[newAddress] = address[1].to_i(2)}}
puts memory.values.sum