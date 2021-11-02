#Day 9
def dive(stream, index, level):
	junk = False
	sub_score = 0
	junk_count = 0
	while index < len(stream):
		if stream[index] == '!': index += 1
		elif junk:
			if stream[index] == '>':
				junk = False
			else:
				junk_count += 1
		else:
			if stream[index] == '<':
				junk = True
			elif stream[index] == '}': return level + sub_score, index, junk_count
			elif stream[index] == '{':
				result = dive(stream, index+1, level+1)
				sub_score, index, junk_count = result[0]+sub_score, result[1], result[2] + junk_count
		index += 1
	return sub_score, junk_count

with open('day9.txt') as infile:
	stream = infile.read()

result = dive(stream, 0, 0)
print (result[0])
#part 2
print (result[1])