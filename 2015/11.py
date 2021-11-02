from re import search

password = 'cqjxjnds'

def increment(password, index):
	if password[index] != 'z':
		password = password[:index] + chr(ord(password[index])+1) + password[index+1:]
		return password
	else:
		temp_word = increment(password, index-1)
		return temp_word[:index] + 'a' + temp_word[index+1:]

def check_validity(password):
	doubles = search(r'(?=(\w)\1\w*(\w)\2)\w+', password)
	iol = search(r'(?!\w*(i|o|j))\w+', password)
	triple = False
	for i in range(len(password)-2):
		if ord(password[i]) == ord(password[i+1])-1 and ord(password[i]) == ord(password[i+2])-2:
			triple = True
	return (iol and doubles and triple)

while not check_validity(password):
	password = increment(password, len(password)-1)

print (password) #part 1: dont know why i decided to go recursive, but i tried to use global variables which was stupid and cost me time

password = increment(password, len(password)-1)

while not check_validity(password):
	password = increment(password, len(password)-1)

print (password) #part 2: pretty self explanitory, just re ran process to find next acceptable password