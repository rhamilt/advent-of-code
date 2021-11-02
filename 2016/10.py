import re

def parse(instrucs):
	bots = {}
	dests = {}
	for instruc in instrucs:
		if instruc.startswith('value'): #Instruc starts with 'value'
			value, target_bot = map(int, re.findall(r'\d+', instruc))
			if target_bot not in bots:
				bots[target_bot] = []
			bots[target_bot].append(value)
		else:
			original_bot, low_bot, high_bot = map(int, re.findall(r'\d+', instruc))
			out_low, out_high = re.findall(r' (bot|output)', instruc) # space to avoid first "bot"
			dests[original_bot] = ((out_low, low_bot), (out_high, high_bot))
	return bots, dests

def solve(bots, dests):
	outputs = {}
	while bots:
		for starting_bot, data in bots.items():
			if len(bots[starting_bot]) == 2:
				low, high = sorted(bots.pop(starting_bot))
				if ((low, high) == (17, 61)): print (starting_bot) #part 1 return
				(out_low, low_bot), (out_high, high_bot) = dests[starting_bot]

				if (out_low) == 'bot':
					if low_bot not in bots:
						bots[low_bot] = []
					bots[low_bot].append(low)
				else:
					outputs[low_bot] = low
				if (out_high) == 'bot':
					if high_bot not in bots:
						bots[high_bot] = []
					bots[high_bot].append(high)
				else:
					outputs[high_bot] = high
					
				break
	print (outputs[0]*outputs[1]*outputs[2])
				
def main():
	instrucs = list(map(str.strip,open('10.txt', 'r').readlines()))
	bots, dests = parse(instrucs)

	solve(bots, dests) #part 1: ok ngl this problem was mad confusing to me because I didn't understand the order. Of course I made an 17 == '17' mistake too
					   #part 2: 

if __name__ == '__main__':
	main()