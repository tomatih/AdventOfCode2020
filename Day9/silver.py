#!/usr/bin/env python

sample_size = 25
memory = list()


with open("input.txt") as f:
	for i,line in enumerate(f.readlines()):
		val = int(line)
		if i < sample_size:
			memory.append(val)
		else:
			have_found = False
			for x in range(sample_size):
				for y in range(x+1,sample_size):
					if memory[x]+memory[y] == val:
						have_found = True
			if not have_found:
				print(val)
				quit()
			memory = memory[1:]+[val]
