#!/usr/bin/env python

memory = dict()
floating = list()

def do_aflip(adr, pos_i):
	to_return = []
	adr[floating[pos_i]] = "0"
	if pos_i == len(floating)-1:
		to_return.append(int("".join(adr),2))
	else:
		to_return += do_aflip(adr,pos_i+1)

	adr[floating[pos_i]] = "1"
	if pos_i == len(floating)-1:
		to_return.append(int("".join(adr),2))
	else:
		to_return += do_aflip(adr,pos_i+1)

	return to_return



with open("input.txt") as file:
	for line in file:
		if line.startswith("mask"):
			mask = line.split(" ")[-1].strip()
			floating=list()
			for i,a in enumerate(mask):
				if a == "X":
					floating.append(i)
		else:
			adress = int(line[4:].split(']')[0])
			val = int(line.split(" ")[-1])
			adress_b = bin(adress)[2:]
			adress_b = "0"*(len(mask)-len(adress_b))+adress_b
			adress_b = list(adress_b)
			# apply symbols
			for i,m in enumerate(mask):
				if m == "1":
					adress_b[i] = '1'
				elif m=='X':
					adress_b[i] = 'X'
			for adr in do_aflip(adress_b,0):
				memory[adr] = val
			


print(sum(memory.values()))
