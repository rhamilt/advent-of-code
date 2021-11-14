lines = File.open("4.txt").readlines.map(&:strip).sort!
#puts lines
guards = {}
minutesFreq = Hash.new(0)
#parse
guard = 0
awake = true #T if awake, F if sleepyhead
lastTime = 0
lines.each do |line|
	m = line.match /\[(\d{4})-(\d\d)-(\d\d) \d\d:(\d\d)\] (.*)/
	year, month, day, minute, action = m[1].to_i,m[2].to_i,m[3].to_i,m[4].to_i,m[5]
	aM = action.match /#(\d+)/
	if aM
		guard = aM[1].to_i
		awake = true
		guards[guard] = {} if !guards.keys.include? guard
	else
		if action.include? "falls"
			awake = false
		else
			awake = true
			for i in (lastTime..minute-1) do 
				guards[guard][i] = 0 if !guards[guard].keys.include? i
				guards[guard][i] += 1
			end
		end
	end
	lastTime = minute
end

=begin
	This took me a lot longer than it should have because A) I didn't realize input wasn't sorted and
	B) I tried to do a lot of default dict type shenanigans with Hash.new(Hash.new) (which apparently 
	does not work). Once I got all of that sorted out my sleepiest guard/minute method worked well
=end
def method1(guards)
	sleepiestGuard = guards.max_by{|guard, minutes| minutes.values.sum}[0] #Gives number of sleepiest guard
	sleepiestMinute =  guards[sleepiestGuard].max_by{|minute, freq| freq}[0]
	p sleepiestGuard * sleepiestMinute
end
=begin
	Ok ngl this took me probably longer than it should have. Based on the way I stored everything,
	it was actually pretty simple, but the stupid max_by method alwasy returns as [key, val], so I 
	was constantly forgetting to subscript the output
=end
def method2(guards)
	sleepiestMinutes = {}
	guards.each do |guard, minutes|
		sleepiestMinutes[guard] = minutes.max_by{|minute, freq| freq} if minutes != {}
	end
	sleepiestGuard = sleepiestMinutes.max_by {|guard, sleepiestMinute| sleepiestMinute[1]}[0]
	p sleepiestGuard * sleepiestMinutes[sleepiestGuard][0]
end

method1(guards)
method2(guards)