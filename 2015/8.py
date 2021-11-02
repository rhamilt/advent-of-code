lines = list(map(str.strip, open('8.txt', 'r').readlines()))

literal_length = sum([len(line) for line in lines])
memory_lengths = []

for line in lines:
	string = line[1:-1]
	temp_string = ''
	char = 0
	while char < len(string):
		if string[char] == '\\':
			if string[char+1] == 'x':
				temp_string += ' '
				char += 4
			else:
				temp_string += string[char+1]
				char += 2
		else: 
			temp_string += string[char]
			char += 1
	memory_lengths.append(len(temp_string))

print (literal_length-sum(memory_lengths)) #part 1: couple bugs here and there, could have been faster and more elegant

encoded_lengths = []

for string in lines:
	temp_string = ''
	char = 0
	while char < len(string):
		if string[char] == '\"':   temp_string += '\\\"'
		elif string[char] == '\\': temp_string += '\\\\'
		else: 					   temp_string += string[char]
		char += 1
	encoded_lengths.append(len(temp_string)+2) #+2 for beginning and ending quotes

print (sum(encoded_lengths) - literal_length) #part 2: super straightforward