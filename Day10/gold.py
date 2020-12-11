#!/usr/bin/env python

with open("input.txt") as f:
	data = sorted([int(x) for x in f.readlines()])

data = [0]+data
data = data+[data[-1]+3]

tree = list()
for i in range(len(data)-1):
	conns = list()
	delta = data[i+1]-data[i]
	conns.append(1)
	if i<len(data)-2:
		delta = data[i+2]-data[i]
		if delta == 2 or delta == 3:
			conns.append(2)
	if i<len(data)-3:
		delta = data[i+3]-data[i]
		if delta == 3:
			conns.append(3)
	tree.append(conns)

accumulator = 0
def go_down(index,target):
	if index==target:
		global accumulator
		accumulator +=1
		return
	for a in tree[index]:
		go_down(index+a,target)

answers = list()
last_index = -1
for i in range(len(tree)):
	if len(tree[i]) != 1 and last_index == -1:
		last_index = i
	elif len(tree[i]) == 1:
		if last_index != -1:
			#print("done search",last_index,i)
			accumulator = 0
			go_down(last_index,i+1)
			answers.append(accumulator)
			last_index=-1
out = 1
for val in answers:
	out *= val

print(out)
