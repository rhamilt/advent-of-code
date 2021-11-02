class Computer
	def initialize(file, noun=nil, verb=nil) 
		@init_lines = File.read(file).split(",").map(&:to_i)
		if !noun.nil?
			@init_lines[1] = noun
			@init_lines[2] = verb
		end
	end

	def printLines
		print @init_lines
		puts
	end

	def opcode(input=0)
		idx = 0
		lines = @init_lines.clone
		while idx < lines.length
			## Regex to capture opcode and parameters
			rgx = /(?<m3>\d)??(?<m2>\d)?(?<m1>\d)\d(?<opcode>\d)$|(?<opcode>\d)$/
			captures = lines[idx].to_s.match(rgx).named_captures
			## Converting parameters into vals based on parameter vs literal mode
			m1, m2, m3 = captures['m1'].to_i, captures['m2'].to_i, captures['m3'].to_i
			m1 != 1 ? parameter1 = lines[lines[idx + 1]]: parameter1 = lines[idx + 1]
			m2 != 1 ? parameter2 = lines[lines[idx + 2]]: parameter2 = lines[idx + 2]
			parameter3 = lines[idx + 3]
			## OPCODES
			case captures['opcode'].to_i
			when 1 #add
				lines[parameter3] = parameter1 + parameter2
				idx += 4
			when 2 #multiply
				lines[parameter3] = parameter1 * parameter2
				idx += 4
			when 3 #input
				lines[lines[idx + 1]] = input
				idx += 2
			when 4 #output
				return parameter1 if parameter1 != 0
				idx += 2
			when 5 #jump-if-true
				if parameter1 != 0
					idx = parameter2 - 3
				end
				idx += 3
			when 6 #jump-if-false
				if parameter1 == 0
					idx = parameter2 - 3
				end
				idx += 3
			when 7 #less than
				lines[parameter3] = parameter1 < parameter2 ? 1 : 0
				idx += 4
			when 8 #equals
				#puts "CODE 8"
				lines[parameter3] = parameter1 == parameter2 ? 1 : 0
				idx += 4
			else
				break
			end
		end
		return lines[0]
	end

	def nounVerb(total)
		save_lines = @init_lines.clone
		99.times do |n|
			99.times do |v|
				@init_lines[1] = n
				@init_lines[2] = v
				if opcode == total
					return 100 * n + v
				end
			end
		end
		@init_lines = save_lines
	end

	def amplification_circuit

	end
end