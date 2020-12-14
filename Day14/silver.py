#!/usr/bin/env python

memory = dict()
mask = str()

with open("input.txt") as f:
	for line in f:
		if line.startswith("mask"):
			mask = line.split(" ")[-1].strip()
		else:
			adress = int(line[4:].split(']')[0])
			val_r = int(line.split(" ")[-1])
			val_b = bin(val_r)[2:]
			val_b = "0"*(len(mask)-len(val_b))+val_b
			val_b = list(val_b)
			for i,m in enumerate(mask):
				if m == "1":
					val_b[i] = '1'
				elif m=='0':
					val_b[i] = '0'
			val_b = "".join(val_b)
			val = int(val_b,2)
			memory[adress] = val

print(sum(memory.values()))
