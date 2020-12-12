#!/usr/bin/env python

checker = [0 for x in range(ord('a'), ord('z')+1)]
offset = ord('a')
out = 0
group_l = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if not len(line):
            # end of group
            for i in range(len(checker)):
                if group_l == checker[i]:
                    out += 1
                checker[i] = 0
            group_l = 0
        else:
            group_l += 1
            for letter in line:
                checker[ord(letter)-offset] += 1

print(out)
