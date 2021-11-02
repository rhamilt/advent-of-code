load "Computer.rb"
'''
def opcode(noun, verb)
	lines = File.read("day2.txt").split(",").map(&:to_i)
	lines[1] = noun
	lines[2] = verb
	idx = 0
	while idx < lines.length
		opcode = lines[idx]
		case opcode
		when 1
			lines[lines[idx + 3]] = lines[lines[idx + 1]] + lines[lines[idx + 2]]
		when 2
			lines[lines[idx + 3]] = lines[lines[idx + 1]] * lines[lines[idx + 2]]
		end
		idx += 4
	end
	return lines
end

def nounVerb
	99.times do |n|
		99.times do |v|
			if opcode(n, v)[0] == 19690720
				return 100 * n + v
			end
		end
	end
end

puts opcode(12, 2)[0] #part 1
puts nounVerb
'''

computer = Computer.new('day2.txt', 12, 2)
puts computer.opcode
puts computer.nounVerb(19690720)