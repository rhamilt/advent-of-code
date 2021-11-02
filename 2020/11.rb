DXY = [-1, 0, 1].freeze

def run(lines, p2)
	temp = ""
	(0..lines.size-1).each do |row|
		(0..lines[row].size-1).each do |col|
			temp << nearby(row, col, lines, p2)
		end
		yield temp
		temp = ""
	end
	return temp
end

def nearby(row, col, lines, p2)
	seat = lines[row][col]
	return seat if seat == "."
	count = 0
	
	9.times do |i|
		diff = [DXY[i / 3], DXY[i % 3]]
		r = row + diff[0]
		c = col + diff[1]
		inRange = lambda { |r, c| r.between?(0,92) && c.between?(0,94)} #saving space
		if !p2
			if inRange.call(r, c)
				count += 1 if lines[r][c] == "#"
			end
		else
			while inRange.call(r, c)
				count += 1 if lines[r][c] == "#"
				break if lines[r][c] == "L" || lines[r][c] == "#"
				r += diff[0]
				c += diff[1]
			end
		end
	end

	max = p2 ? 6: 5 #+1 because I counted the current seat
	case seat
	when "L"
		return count == 0 ? "#": "L"
	else
		return count < max ? "#": "L" 
	end
end

lines = File.open("11.txt").read.split("\n")
p2 = false
2.times do |i|
	nSeats, temp = lines[0..-1], []
	while nSeats != temp
		temp = nSeats[0..-1]
		nSeats = []
		run(temp, p2) {|row| nSeats << row}
	end
	puts nSeats.map {|row| row.count "#"}.sum
	p2 = !p2
end