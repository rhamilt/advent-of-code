p1Raw, p2Raw = File.open("21.txt").read.split("\n")
p1Idx = 8
p2Idx = 7
p1, p2 = 0, 0
dieRolls = 0
die = 0
while p1 < 1000 and p2 < 1000
	tot = 0
	3.times do 
		die = (die) % 100 + 1
		tot += die
	end
	dieRolls += 3
	p1Idx = (p1Idx+tot-1) % 10 + 1
	p1 += p1Idx
	break if p1 >= 1000
	tot = 0
	3.times do 
		die = die % 100 + 1
		tot += die
	end
	dieRolls += 3
	p2Idx = (p2Idx+tot-1) % 10 + 1
	p2 += p2Idx
end

p (dieRolls * [p1, p2].min)

p1Idx = 8
p2Idx = 7
p1, p2 = 0, 0

def addPossibles(idx, poss)
	poss[(idx+2)%10+1] += 1
	poss[(idx+3)%10+1] += 3
	poss[(idx+4)%10+1] += 6
	poss[(idx+5)%10+1] += 6
	poss[(idx+6)%10+1] += 3
	poss[(idx+7)%10+1] += 1
	return poss
end
poss1 = addPossibles(p1Idx, Hash.new(0))
poss2 = addPossibles(p2Idx, Hash.new(0))
p poss2
winner1 = 0
winner2 = 0
while poss1.values.sum != 0 and poss2.values.sum != 0
	
end