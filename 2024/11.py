stones = open("11.txt").read().split()

##### Brute solution for fun
# def step(i):
#     if not int(i):
#         return ["1"]
#     elif not (len(i) % 2):
#         return [i[len(i)//2:], i[:len(i)//2]]
#     else:
#         return [str(2024 * int(i))]

# brute = [s for s in stones]
# for i in range(25):
#     brute = sum((step(s) for s in brute), [])
# print (len(stones))

seen = {}
def calc(s, n):
    if n == 0:
        return 1
    if (s, n) in seen:
        return seen[s, n]
    if not int(s):
        seen[s, n] = calc("1", n - 1)
    elif not (len(s) % 2):
        seen[s, n] = calc(str(int(s[len(s)//2:])), n - 1) + calc(str(int(s[:len(s)//2])), n - 1)
    else:
        seen[s, n] = calc(str(2024 * int(s)), n - 1)
    return seen[s, n]

# 22 ms
print (sum(calc(s, 25) for s in stones))
# 150 ms
print (sum(calc(s, 75) for s in stones))
