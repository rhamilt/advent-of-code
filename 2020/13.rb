myTime, busList = File.open("13.txt").read.split("\n")
busOrder = busList.split(",")
buses = busOrder.select {|x| x != "x"}

time = 0
while true
	possible = buses.select {|bus| (myTime.to_i + time) % bus.to_i == 0}
	break if possible.size > 0
	time += 1
end
puts possible[0].to_i * time

time, increment = 0, buses[0].to_i
(busOrder.index(increment.to_s) + 1...busOrder.size).each do |bus|
	next if busOrder[bus] == "x"
	while (time + bus) % busOrder[bus].to_i != 0
		time += increment
	end
	increment *= busOrder[bus].to_i
end
puts time