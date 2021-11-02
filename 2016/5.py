import hashlib

doorID = open('5.txt', 'r').read()
password1 = []
password2 = ['*' for i in range(8)]

n = 0
while '*' in password2:
	string = doorID + str(n)
	md5 = hashlib.md5(string.encode()).hexdigest()
	if md5.startswith('00000'):
		if len(password1) < 8: password1.append(md5[5])
		if int(md5[5], 16) < 8 and password2[int(md5[5])] == '*': 
			password2[int(md5[5])] = md5[6]
	n += 1

print (''.join(password1)) #part 1: simple once i learned how to do md5, made mistake of thinking that there had to be leading 0s before n
print (''.join(password2)) #part 2: took a while, both execution and coding, don't know what i fixed to make it work
