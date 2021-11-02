lines = list(map(str.strip, open('2.txt', 'r').readlines()))
sas = []
for line in lines:
	l, w, h = tuple(list(map(int,line.split('x'))))
	slack = min([l*w,l*h, w*h])
	sas.append(2*(l*w + l*h + w*h)+slack)
print (sum(sas)) #part 1: spent a little bit of time until i realized had to include slack calc (size of smallest side)

ribbons = []
for line in lines:
	l, w, h = tuple(list(map(int,line.split('x'))))
	bow = l*w*h
	temp = sorted([l,w,h])
	ribbon = 2*(temp[0] + temp[1])
	ribbons.append(ribbon+bow)
print (sum(ribbons))#part 2: took a little bit of time thinking how to get smallest two side, ended up using ugly temp variable