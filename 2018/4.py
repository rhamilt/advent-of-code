from collections import defaultdict, Counter
class timeStamp():
   def __init__(self, string):
      self.year = '1518'
      self.string = string
      self.month = string[string.index("-")+1: string.index("-")+3]
      self.day = string[string.index(" ")-2: string.index(" ")]
      self.hour = string[string.index(':')-2: string.index(":")]
      self.minute = string[string.index(':')+1: string.index("]")]
      if '#' in string:
         self.guardNum = string[string.index("#")+1:string.index("begins")]
      elif 'falls' in string:
      	self.asleep = (True)
      else:
         self.asleep = (False)
   def __lt__(self, other):
   	  return (self.month*30 + 24*self.day + 60*self.hour + self.minute) < (other.month*30 + other.day*24 + 60*other.hour + other.minute)
      
with open('day4_input.txt', 'r') as infile:
   lines = infile.read().splitlines()
times = []
guards = {0:0}
guardss = defaultdict(list)
for line in lines:
   times.append(timeStamp(line))
times = sorted(times)
currGuard, start, end = 0,0,0
for time in times:
	print (time.string)
	if '#' in time.string:
		if time.guardNum not in guards:
			guards[time.guardNum] = 0
		currGuard = time.guardNum
	elif time.asleep:
		start = time.minute
	elif not time.asleep:
		end = time.minute
		for x in range(int(start), int(end)):
			guardss[currGuard].append(x)
		guards[currGuard] += (int(end)-int(start))
minute, count = Counter(guardss['3323 ']).most_common(1)[0]
print (minute*3323)
#Part 2
print (guardss)
maxi = ('', 0)
print (maxi)
for each in guardss:
	q_table = {}
	for minute in guardss[each]:
		if minute not in q_table:
			q_table[minute] = 0
		q_table[minute] += 1
	print (q_table)
	if max([(v, k) for (k, v) in q_table.items()])[0] > maxi[1]:
		maxi = (each, max([(v, k) for (k, v) in q_table.items()])[0])
print(maxi)



