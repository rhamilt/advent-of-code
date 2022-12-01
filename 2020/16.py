import re
from collections import defaultdict
from functools import reduce

[info, myTicket, otherTickets] = open("16.txt").read().strip().split("\n\n")

# Get a set of ints of the range from a tuple of strings
# eg {1, 2, 3, 4} from ('1', '4')
def get_range_set(rng):
    [lo, hi] = list(map(int, rng))
    return set(i for i in range(lo, hi + 1))

# Parse the possible ranges of the fields into a total set of possible ranges and a dictionary of
# ranges corresponding to the field names
total_range_set = set()
fields = {}
for field in info.split('\n'):
    field_name = re.search(r'(.+):', field).group(1)
    field_range_set = set()
    for rng in re.findall(r'(\d+)-(\d+)', field):
        field_range_set = field_range_set.union(get_range_set(rng))
    total_range_set = total_range_set.union(field_range_set)
    fields[field_name] = field_range_set

# Parse ticket into list of ints from string
def getTicket(ticket_str):
    return list(map(int, ticket_str.split(',')))

myTicket = getTicket(myTicket.split('\n')[1])

otherTickets = [getTicket(ticket) for ticket in otherTickets.split('\n')[1:]]

# Calculate ticket error scanning rate and keep the tickets that are valid tickets
ticketErrorScanningRate = 0
properTickets = []
for ticket in otherTickets:
    proper = True
    for val in ticket:
        if val not in total_range_set:
            ticketErrorScanningRate += val
            proper = False
    if proper: properTickets.append(ticket)

# Part 1: No issues, pretty easy to parse all the input
print (ticketErrorScanningRate)

# Narrow down the list of fields that could possibly work with a given position on a ticket
# The result is that there is one position on the ticket that can only be 1 field, one position
# that can only be 2 fields, and so on up to 19.
validFields = defaultdict(lambda: set(fields.keys()))
for ticket in properTickets + [myTicket]:
    for field_num in range(len(ticket)):
        for (field_name, field_range) in fields.items():
            if ticket[field_num] not in field_range:
                validFields[field_num].remove(field_name)

# Use process of elimination to figure out which fields correspond to which ticket positions
field_name_to_num = {}
while len(field_name_to_num) < 19:
    for (field_num, valid) in validFields.items():
        # Check if this field is the only possible one at this position
        if len(valid) == 1:
            field_name = valid.pop()
            field_name_to_num[field_name] = field_num
            # Remove this as a possibility from other ticket positions
            for other_valid in validFields.values():
                if field_name in other_valid:
                    other_valid.remove(field_name)

departure_fields = [myTicket[field_num] \
                    for (field_name, field_num) in field_name_to_num.items() \
                    if "departure" in field_name]

# Part 2: Once I actually got to sit down and think about this, it actually came pretty naturally
# for me to solve. Surprisingly got it first try with no mistakes. I think that came because there
# was no time pressure and I was very focused
print (reduce(lambda a, b: a * b, departure_fields))