from re import search
import itertools

def parse(instruc):
	s1 = search(r'^(\S+) -> (\w+)', instruc)
	if s1:
		return (-1, -1, s1.group(1), '', s1.group(2))
	s2 = search(r'((\S*)\s)*([A-Z]+) (.+) -> (.+)', instruc)
	return (s2.group(2), s2.group(4), '*', s2.group(3), s2.group(5)) #(input1, input2, passed value, operator, destination)

def cycle(instrucs, circuit):
	for instruc in itertools.cycle(instrucs):
		if instruc[4] not in circuit and (instruc[0] in circuit or instruc[1] in circuit or instruc[0] == -1):
			if instruc[3] == "AND" and instruc[0] in circuit and instruc[1] in circuit:
				circuit[instruc[4]] = circuit[instruc[0]] & circuit[instruc[1]]
			elif instruc[3] == "OR" and instruc[0] in circuit and instruc[1] in circuit:
				circuit[instruc[4]] = circuit[instruc[0]] | circuit[instruc[1]]
			elif instruc[3] == "LSHIFT" and instruc[0] in circuit:
				circuit[instruc[4]] = circuit[instruc[0]] << int(instruc[1])
			elif instruc[3] == "RSHIFT" and instruc[0] in circuit:
				circuit[instruc[4]] = circuit[instruc[0]] >> int(instruc[1])
			elif instruc[3] == "NOT" and instruc[1] in circuit:
				circuit[instruc[4]] = ~circuit[instruc[1]] & 0xffff
			else:
				try:
					circuit[instruc[4]] = int(instruc[2])
				except:
					if instruc[2] in circuit:
						circuit[instruc[4]] = circuit[instruc[2]]

		if len(circuit)-1 == len(instrucs):
			return circuit

upinstrucs = list(map(str.strip, open('7.txt', 'r').readlines()))
instrucs = []
for upinstruc in upinstrucs:#up is unparsed
	instrucs.append(parse(upinstruc))

aval = cycle(instrucs, {"1" : 1})['a']

print (aval) #part 1: this took me a brick because i tried to get cute instead of making elif chain
print (cycle(instrucs, {'1': 1, 'b': aval})['a']) #part 2: much easier, just made a method to cycle the circuit
