from re import match

lines = list(map(str.strip, open("2.txt").readlines()))

count = 0
for line in lines:
    m = match(r"(\d*)-(\d*) (\w): (\w+)", line)
    mini, maxi, char, string = m.group(1), m.group(2), m.group(3), m.group(4)
    char_count = string.count(char)
    if char_count >= int(mini) and char_count <= int(maxi):
        count += 1

# part 1: again, pretty straight forward
print (count)

count = 0
for line in lines:
    m = match(r"(\d*)-(\d*) (\w): (\w+)", line)
    mini, maxi, char, string = m.group(1), m.group(2), m.group(3), m.group(4)
    if string[int(mini)-1] == char ^ string[int(maxi)-1] == char:
        if string[int(mini)-1] != char or string[int(maxi)-1] != char:
            count += 1
# part 2: I am doing this on the plane, but I would use xor if I knew how in python
print(count)