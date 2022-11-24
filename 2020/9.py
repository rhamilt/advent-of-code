nums = list(map(int, open('9.txt').read().split('\n')))

def sum_to(preamble, num):
    for i in range(len(preamble)):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == num: return True
    return False

idx = 25
while idx < len(nums):
    if not sum_to(nums[idx-25:idx], nums[idx]): break
    idx += 1

invalid_number = nums[idx]
# part 1: pretty easy, did it pretty quickly
print (invalid_number)

window = 1
idx = 1
window_arr = []
while idx + window < len(nums):
    while sum(nums[idx:idx + window + 1]) < invalid_number:
        window += 1
    if sum(nums[idx:idx + window + 1]) == invalid_number:
        window_arr = nums[idx:idx + window + 1]
        break
    idx += 1
    window = 1

# part 2: also did this one quickly
print (max(window_arr) + min(window_arr))