def check(boards)
	winners = []
	boards.each do |board|
		#p board
		board[0].each_index do |c|
			col = ""
			board.each_index do |r|
				winners << board if board[r].join("") == "_____"
				col << board[r][c]
			end
			winners << board if col == "_____"
		end
	end
	return winners
end

def score(board, number)
	total = 0
	(0...board.length).each do |r|
		(0...board[0].length).each do |c|
			total += board[r][c].to_i if board[r][c] != "_"
		end
	end
	return total * number.to_i
end

lines = File.open("4.txt").read.split("\n\n").map(&:strip)#.map(&:to_i)
nums = lines[0]
boardStrings = lines[1..]
boards = []

boardStrings.each do |board|
	boards << board.split("\n").map(&:split)
end

overallWinners = []
nums.split(",").each do |num|
	boards.each do |board|
		board.each_index do |r|
			board[r].each_index do |c|
				board[r][c] = "_" if num == board[r][c]
			end
		end
	end

	winners = check boards
	winners.each do |winner|
		boards.delete winner
		overallWinners << [winner, num]
	end
	break if boards.size == 0
end

=begin part1
	Embarrasing. I think in the future I need to look for the clever way to do things instead of
	rushing in feet first. Leo showed a clever way to do it but I was too caught up in the "regular" way
=end
p score overallWinners[0][0],overallWinners[0][1].to_i
=begin part2
	Embarrasing again. If only I knew that multiple boards could be matched at once LOL... took me much too
	long to figure that out.
=end
p score overallWinners[-1][0],overallWinners[-1][1].to_i
