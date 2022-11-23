import re

passports = list(map(str.split, open('4.txt').read().split("\n\n")))

def valid_num_fields(passport):
    if len(passport) == 8:
        return True
    elif len(passport) == 7:
        for field in passport:
            if "cid" in field:
                return False
        return True
    return False

# part 1: Straightforward, only need to count the fields
print (sum([1 for passport in passports if valid_num_fields(passport)]))

count = 0
for passport in passports:
    if not valid_num_fields(passport): continue
    valid = True
    for field in passport:
        [fieldName, fieldValue] = field.split(":")
        if fieldName == "byr":
            if int(fieldValue) < 1920 or int(fieldValue) > 2002: valid = False
        if fieldName == "iyr":
            if int(fieldValue) < 2010 or int(fieldValue) > 2020: valid = False
        if fieldName == "eyr":
            if int(fieldValue) < 2020 or int(fieldValue) > 2030: valid = False
        if fieldName == "hgt":
            num = int(re.search(r'\d+', fieldValue).group())
            if fieldValue.endswith('cm'): 
                if num < 150 or num > 193: valid = False
            elif fieldValue.endswith('in'):
                if num < 59 or num > 76: valid = False
            else: valid = False
        if fieldName == "hcl":
            if not re.match(r'#[0-9a-f]{6}', fieldValue): valid = False
        if fieldName == "ecl":
            if not re.match(r'(amb|blu|brn|gry|grn|hzl|oth)', fieldValue): valid = False
        if fieldName == "pid":
            if not re.match(r'^\d{9}$', fieldValue): valid = False
    if valid: count += 1

# part 2: For some reason this took me quite a long time, lots of off by one errors that forced me
# to restart. Final error was accepting pid with 10 digits, had to force to check that it was 9
print (count)
