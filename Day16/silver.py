#!/usr/bin/env python

section = 0
tester = "lambda a : "
accumulator = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            section += 1
            continue
        if section == 0:
            vals = line.split(":")[1].strip()
            vals = vals.replace("-", "<=a<=")
            vals = f"({vals}) or "
            tester += vals
        elif section == 1:
            if type(tester) == str:
                tester = tester[:-3]
                tester = eval(tester)
        elif section == 2:
            if line.startswith("nearby"):
                continue
            for val in line.split(","):
                val = int(val)
                if not tester(val):
                    accumulator += val

print(accumulator)
