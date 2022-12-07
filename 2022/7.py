from collections import defaultdict

lines = open("7.txt").read().strip().split("\n")

def go_down_level(dir):
    return "/".join(dir.split("/")[:-2]) + "/"

def go_up_level(curr, dir_name):
    return curr + dir_name + "/"

fs = defaultdict(lambda: [])
dir_sizes = defaultdict(lambda: 0)
curr = ""
i = 0
while i < len(lines):
    # Parse cd commands
    while "cd" in lines[i]:
        [_, _, name] = lines[i].split()
        if name == "/": curr = "/"
        elif name == "..": curr = go_down_level(curr)
        else: curr = go_up_level(curr, name)
        i += 1
    i += 1

    # Parse ls command output
    while i < len(lines) and "$" not in lines[i]:
        elem = lines[i]
        if "dir" in elem:
            [_, name] = elem.split()
            fs[curr].append(go_up_level(curr, name))
        else:
            temp_curr = curr
            [file_size, file_name] = elem.split()
            while temp_curr != "/":
                dir_sizes[temp_curr] += int(file_size)
                temp_curr = go_down_level(temp_curr)
            dir_sizes["/"] += int(file_size)
        i += 1

# Part 1: Disaster. First, I copied over all the code I wrote with `cp shell.py 7.py`. Then my
# internet stopped working for the rest of the night. I actually did surprisingly well, although
# the duplicate directory names ended up tripping me up a little bit. Instead I just stored the
# name of the absolute path
print (sum(size for size in dir_sizes.values() if size <= 100000))

unused_space = 70000000 - dir_sizes["/"]
# Part 2: I can't blame anything else for slowness on this one, I think I just didn't quite grasp
# what it was asking for at first.
print (min(size for size in dir_sizes.values() if size >= 30000000 - unused_space))