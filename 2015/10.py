def looknsay(string):
	idx = 0
	temp_idx = 0
	new_string = ''
	while idx < len(string):
		while temp_idx < len(string) and string[temp_idx] == string[idx]:
			temp_idx += 1
		new_string += str(temp_idx-idx) + string[idx]
		idx = temp_idx
	return new_string


string = '1113222113' #input

for i in range(50):
	string = looknsay(string)
	
print (len(string)) #part 1: pretty simple stuff, made a couple indexing errors that added to the time
					#part 2: i thought this was one where you couldnt just brute force through 50, but it actually didnt take long 
					#took much longer to look online for a clean way to calculate solution

CONWAY_CONSTANT = 1.303577269034 #https://www.youtube.com/watch?v=ea7lJkEhytA