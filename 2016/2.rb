lines = File.open("2.txt").readlines.map(&:strip)#.map(&:to_i)
grid1 = [[1,2,3],[4,5,6],[7,8,9]]
grid2 = [[0,0,1,0,0],
		[0,2,3,4,0],
		[5,6,7,8,9],
		[0,0xA,0xB,0xC,0],
		[0,0,0xD,0,0]]
result1 = ""
result2 = ""

r, c, r2, c2 = 1, 1, 2, 2
lines.each_index do |i|
	lines[i].each_char do |char|	
		case char
		when "U"
			r = [0,r-1].max
			r2 = r2-1 if r2 > 0 and grid2[r2-1][c2] != 0
		when "D"
			r = [r+1,2].min
			r2 = r2+1 if r2 < 4 and grid2[r2+1][c2] != 0
		when "L"
			c = [0,c-1].max
			c2 = c2-1 if c2 > 0 and grid2[r2][c2-1] != 0
		when "R"
			c = [c+1,2].min
			c2 = c2+1 if c2 < 4 and grid2[r2][c2+1] != 0
		end
	end
	result1 += grid1[r][c].to_s
	result2 += grid2[r2][c2].to_s(16).upcase
end

=begin part 1
	Took me longer than I would have liked, but it is what it is. I like how I used max though. Probably would
	have done pretty terribly if I had done this day of.
=end
puts result1

=begin part 2
	Same approach to part 1, just added the condition that it couldn't be 0, which I thought was clever.
	Didn't take too long but a little while to type out the full grid
=end
puts result2