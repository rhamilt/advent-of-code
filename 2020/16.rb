info, myTicket, nearby = File.open("16.txt").read.split("\n\n")
ranges = []
info.split("\n").each do |field|
	l1, h1, l2, h2 = field.match(/(\d+)-(\d+) or (\d+)-(\d+)/).captures
	ranges << (l1.to_i..h1.to_i) << (l2.to_i..h2.to_i)
end

notIncluded = []
properNearby = []
nearby.split("\n")[1..-1].each do |ticket|
	fields = ticket.split(",").map(&:to_i)
	legal = true
	(0..fields.size-1).each do |field|
		works = false
		(0..ranges.size-1).each do |range|
			works = true if ranges[range].include? fields[field]
		end
		notIncluded << fields[field] if !works
		legal = false if !works
	end
	properNearby << ticket if legal
end
p notIncluded.sum

properNearby << myTicket.split("\n")[1]
possibleFields = []
p info.size
(0..info.split("\n").size-1).each do |field|
	possibles = nil
	properNearby.each do |ticket|
		currField = ticket.split(",")[field].to_i
		possiblesTemp = []
		(0..ranges.size-1).each do |range|
			#p ranges[range]
			#p currField
			possiblesTemp << range/2 if ranges[range].include? currField
		end
		possibles ||= possiblesTemp
		possibles = possibles & possiblesTemp
	end
	possibleFields << possibles
	p possibleFields
	gets.chomp
end

p possibleFields
order = {}
while possibleFields.map {|x| x.size}.sum > 0
	(0..possibleFields.size-1).each do |field|
		if possibleFields[field].size == 1
			correct = possibleFields[field].pop
			possibleFields.each do |tempField|
				tempField.delete(correct)
			end
			order[field] = correct
		end 
	end
end
departures = []
order.each do |key, val|
	departures << key if val < 6
end
p order
p departures
p departures.inject(:*)