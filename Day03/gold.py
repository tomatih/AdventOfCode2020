#!/usr/bin/env python

slopes = [1, 3, 5, 7, 1]
mods = [1, 1, 1, 1, 2]
hits = [0, 0, 0, 0, 0]
with open("input.txt") as f:
    for i, row in enumerate(f.readlines()):
        row = row.strip()  # sanitaize input
        for j in range(len(slopes)):  # for all slopes
            if i % mods[j]:  # if the slope hits this row
                continue
            # calculate position and sanitise it and look up and compare
            if row[((i//mods[j])*slopes[j]) % (len(row))] == "#":
                hits[j] += 1

# multiply all hit trees
result = 1
for hit in hits:
    result *= hit

print(result)
