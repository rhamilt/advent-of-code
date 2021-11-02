ans = "254032-789860"
ansLow, ansHigh = ans.match(/(\d*)-(\d*)/).captures

def passwordValid(password, p2=false, multipleInRow=[1])
	# Checks if sorted (non decreasing)
	sorted = password == password.sort 
	# Checks if there is an occurence of the same number twice
	# This works because if they're not in order sorted will be false
	multipleInRow = password.sort.map {|x| password.count(x) == 2 ? 1: 0} if p2
	# Returns whether same number back to back
	double = password.join.match(/(\d)\1/)
	return double && multipleInRow.sum > 0 && sorted
end

matches1 = []
matches2 = []
for i in (ansLow.to_i..ansHigh.to_i)
	matches1 << i if passwordValid(i.to_s.split(''))
	matches2 << i if passwordValid(i.to_s.split(''), true) # true for part 2
end

puts matches1.length()
puts matches2.length()