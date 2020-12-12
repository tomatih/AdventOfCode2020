#!/usr/bin/env python

out = [True for x in range(1023)]

# convert to binary
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        Id = int(line
                 .replace('F', '0')
                 .replace('B', '1')
                 .replace('L', '0')
                 .replace('R', '1'), 2)
        out[Id] = False

# trim end
if out[0]:
    for i, v in enumerate(out):
        if not v:
            break
        out[i] = False

# trim front
if out[-1]:
    for i in range(len(out)-1, 0, -1):
        if not out[i]:
            break
        out[i] = False

# print found output
for i, v in enumerate(out):
    if v:
        print(i)
