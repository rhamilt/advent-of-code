def check(curr, p2=false)
	necessary = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
	necessary.each do |x|
		return 0 if !curr.include?(x)
	end
	if p2
		fields = curr.split(' ')
		fields.each do |field|
			code, data = field.split(":")
			case code
				when "byr"
					return 0 if !data.to_i.between?(1920,2002)
				when "iyr"
					return 0 if !data.to_i.between?(2010,2020)
				when "eyr"
					return 0 if !data.to_i.between?(2020,2030)
				when "hgt"
					if data.include? "cm"
						return 0 if !data[..2].to_i.between?(150, 193)
					else
						return 0 if !data[..2].to_i.between?(59, 76)
					end
				when "hcl"
					return 0 if !data.match(/^#[0-9a-f]{6}$/)
				when "ecl"
					return 0 if !['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].include? data
				when 'pid'
					return 0 if !data.match(/^\d{9}$/)
			end
		end
	end
	return 1
end

lines = File.open("4.txt").readlines.map(&:strip)#.map(&:to_i)
curr = ""
cnt1 = 0
cnt2 = 0
lines.each do |line|
	if line == ""
		cnt1 += check(curr)
		cnt2 += check(curr, true)
		curr = ''
	else
		curr << " " + line
	end
end
puts cnt1
puts cnt2