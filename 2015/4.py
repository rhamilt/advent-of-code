from hashlib import md5
input = 'yzbqklnj'
for i in range(100000000):
    h = md5((input + str(i)).encode()).hexdigest()
    if h[:6] == '000000':
        print(i)
        break