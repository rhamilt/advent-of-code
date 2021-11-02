def eval(exp, p2=false)
	if !exp.include? "("
		if !p2
			vals = exp.split
			idx, sum = 1, vals[0].to_i
			while idx < vals.size
				if vals[idx] == "*"
					sum *= vals[idx+1].to_i
				else
					sum += vals[idx+1].to_i
				end
				idx += 2
			end
			return sum
		else
			groups = exp.scan(/\d+ \+ \d+/)
			while groups.size > 0
				groups.each do |addition|
					addition = addition[0..addition.index("+")-1] + '\+' + addition[addition.index("+")+1..-1]
					exp.sub!(/(^| )#{addition}/, '\1' + eval(addition).to_s)
				end
				groups = exp.scan(/\d+ \+ \d+/)
			end
			return eval(exp)
		end
	else
		idx = 0
		simplified = ""
		parenMode = false
		constant = exp[-1] == ")" ? 1: 0
		while idx < exp.size + constant
			if !parenMode
				if exp[idx] == "("
					parenMode = true
					parenCount = 1
					parenIdx = idx + 1
				else
					simplified += exp[idx]
				end
			else
				if parenCount == 0
					simplified += eval(exp[parenIdx..idx-2], p2).to_s + " "
					parenMode = false
				end
				if exp[idx] == "("
					parenCount += 1
				elsif exp[idx] == ")" 
					parenCount -= 1
				end
			end
			idx += 1
		end
		return eval(simplified, p2)
	end
end

lines = File.open("18.txt").read.split("\n")
puts lines.map {|x| eval(x)}.sum
puts lines.map {|x| eval(x, true)}.sum