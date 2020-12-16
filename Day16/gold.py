#!/usr/bin/env python

#!/usr/bin/env python

section = 0
tester = "lambda a : "
fields = dict()
my_ticket = None
possibility_space = dict()
valid_ticket_counter = 0

with open("input.txt") as f:
    for line in f:
        # section separation
        line = line.strip()
        if len(line) == 0:
            section += 1
            continue
        # fields
        if section == 0:
            field_name = line.split(":")[0]
            vals = line.split(":")[1].strip()
            vals = vals.replace("-", "<=a<=")
            fields[field_name] = eval(f"lambda a : {vals}")
            possibility_space[field_name] = list()
            vals = f"({vals}) or "
            tester += vals
        # my ticket
        elif section == 1:
            # crete tester
            if line.startswith("your"):
                tester = tester[:-3]
                tester = eval(tester)
            # save
            else:
                my_ticket = [int(x) for x in line.split(",")]
        # other tickets
        elif section == 2:
            # ignore title line
            if line.startswith("nearby"):
                continue
            # create value list
            vals = [int(x) for x in line.split(",")]
            # check validity
            valid_acc = 0
            for val in vals:
                valid_acc += tester(val)
            # discart invalid
            if valid_acc != len(vals):
                continue
            valid_ticket_counter += 1
            # calculate possiblilty
            for field in fields:
                for i, val in enumerate(vals):
                    if fields[field](val):
                        possibility_space[field].append(i)

# for all fields
for field in possibility_space:
    possibilities = [None for x in range(len(fields.keys()))]
    # chck if they can be represented by each index
    for i in range(len(fields.keys())):
        possibilities[i] = possibility_space[field].count(i) == valid_ticket_counter
    possibility_space[field] = possibilities

# unil all fields are known
for _ in possibility_space:
    # find which fields have certain positions
    can_be_sure = list()
    for field in possibility_space:
        if type(possibility_space[field]) == int:
            continue
        if sum(possibility_space[field]) == 1:
            can_be_sure.append(field)
    # assign values to those fields
    done_filelds = list()
    for field in can_be_sure:
        val = possibility_space[field].index(True)
        done_filelds.append(val)
        possibility_space[field] = val
    # remove that possibility from other fields
    for field in possibility_space:
        if type(possibility_space[field]) == int:
            continue
        for val in done_filelds:
            possibility_space[field][val] = False

# calculate the output
out = 1
for field in possibility_space:
    if field.startswith("departure"):
        out *= my_ticket[possibility_space[field]]
print(out)
