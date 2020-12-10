#!/usr/bin/env python

out = 0

with open('input.txt') as f:
	for line in f.readlines():
		line = line.strip()
		row = int(line[:7].replace('F','0').replace('B','1'),2)
		column = int(line[7:].replace('L','0').replace('R','1'),2)
		out = max(row*8 + column, out)


print(out)