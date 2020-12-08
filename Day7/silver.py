#!/usr/bin/env python

# color: [(contained_by_what, times),...]
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
		for arg in args:
			if arg == "no other":
				continue
			amount = int(arg.split(" ")[0])
			color = " ".join(arg.split(" ")[1:])
			if color in connections:
				connections[color].append((base, amount))
			else:
				connections[color] = [(base,amount)]


# search 
visited = list()

def checker(color):
	if color in visited:
		return
	visited.append(color)
	if color in connections:
		for col,val in connections[color]:
			checker(col)

checker("shiny gold")
print(len(visited)-1) # -1 coz shing gold itself