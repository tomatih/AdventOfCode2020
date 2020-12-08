#!/usr/bin/env python


connections = dict()
split_strip = lambda a,b : [x.strip() for x in a.split(b)]


with open('input.txt') as f:
	for line in f.readlines():
		# remove whitespace
		line = line.strip() 
		# remove language fluff
		line = line.replace("bags","bag")
		line = line.replace("bag","")
		# get base and args
		base, args = split_strip(line,"contain")
		args = args.replace(".","")
		args = split_strip(args,",")
		# bild tree
		if base not in connections:
			connections[base] = list()
		for arg in args:
			if arg == "no other":
				continue
			amount = int(arg.split(" ")[0])
			color = " ".join(arg.split(" ")[1:])
			connections[base].append((color,amount))


def checker(color):
	if len(connections[color]) == 0:
		return 1

	out = 1
	for col,val in connections[color]:
		out += val*checker(col)
	return out

print(checker("shiny gold")-1)

