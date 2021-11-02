def run(lines, p2=false)
	acc = 0
	seen = []
	idx = 0
	while idx < lines.size
		if seen.include? idx
			p acc if !p2
			return
		end
		seen << idx
		cmd, am = lines[idx].split
		amount = am[1..].to_i
		amount *= -1 if am.include? "-"
		case cmd
		when "acc"
			acc += amount
		when "jmp"
			idx += amount - 1 
		end
		idx += 1
	end
	p acc
end

lines = File.open("8.txt").read.split("\n")#.map(&:to_i)
run(lines)
idx = 0
while idx < lines.size
	if !lines[idx].include? "acc"
		temp = lines[0..-1]
		temp[idx] = temp[idx].tr("jmno", "nojm")
		run(temp, true)
	end
	idx += 1
end