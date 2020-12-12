#!/usr/bin/env python

pos = 0
out = 0
with open("input.txt") as f:
    for row in f.readlines():
        row = row.strip()
        if row[pos % len(row)] == "#":
            out += 1
        pos += 3

print(out)
