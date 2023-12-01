lines = open("1.txt").read().strip().split("\n")

nums = []
for line in lines:
    chars = []
    for char in line:
        if char in "0123456789":
            chars.append(char)
    nums.append(int(chars[0] + chars[-1]))


print(sum(nums))

map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

nums = []
for line in lines:
    chars = []
    for i, char in enumerate(line):
        if char in "0123456789":
            chars.append(char)
        else:
            for c in map:
                if i + len(c) <= len(line) and line[i: i + len(c)] == c:
                    chars.append(map[c])
    nums.append(int(chars[0] + chars[-1]))

print(sum(nums))
