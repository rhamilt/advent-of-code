from re import search

def caesar_cypher(n, string):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	decoded = ''
	for char in string:
		if char == '-':
			decoded += ' '
		else:
			decoded += alpha[(alpha.index(char)+n) % len(alpha)]
	return decoded

lines = open('4.txt', 'r').read().split('\n')

total = 0

for line in lines:
	letters, stringID, checksum = search(r'([a-z-]+)+-(\d+)\[(\w{5})\]', line).groups()
	char_dict = {}
	for char in letters.replace('-',''): #takes the main string body, minus the dashes
		if char not in char_dict:
			char_dict[char] = 0
		char_dict[char] += 1

	m_common = sorted(sorted(char_dict.items()), key = lambda x: -x[1])
	if ''.join([char[0] for char in m_common][:5]) == checksum:
		total += int(stringID)
		decoded = caesar_cypher(int(stringID), letters)
		if 'north' in decoded: caesar_room = int(stringID)

print (total) #part 1: ngl, this kicked my ass big time. figured it was best to alphabetize the most common list, then later \
			  # figured out that I could alphabetize the list, and then sort by occurences and it would be all in order
print (caesar_room) # part 2: with the caesar cypher was easier than expected, made one mistake with parens
