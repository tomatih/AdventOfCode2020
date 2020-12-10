#!/usr/bin/env python

checker = [False for x in range(ord('a'),ord('z')+1)]
offset = ord('a')
out = 0

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		if not len(line):
			# end of group
			out += sum(checker)
			checker = [False for x in range(ord('a'),ord('z')+1)]
		else:
			for char in line:
				checker[ord(char)-offset] = True


print(out)