jump = 324

lock = [0]

pos = 0
for i in range(1, 2018):
	pos = (pos + jump) % len(lock) + 1
	lock.insert(pos, i)

print (lock[lock.index(2017)+1])


#part 2
i = 0
for t in range(1,50000000+1):
	i = (i+jump)%t + 1
	if i==1:
		val_after_0 = t
print (val_after_0)
