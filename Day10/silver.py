#!/usr/bin/env python

with open("input.txt") as f:
    data = sorted([int(x) for x in f.readlines()])

data = [0]+data
data = data+[data[-1]+3]
one_jumps = 0
three_jumps = 0

for i in range(len(data)-1):
    if data[i+1] - data[i] == 1:
        one_jumps += 1
    elif data[i+1] - data[i] == 3:
        three_jumps += 1
    elif data[i+1] - data[i] > 3:
        print("SCREAM FOR HELP")

#print("one: ",one_jumps,"three: ", three_jumps)
print(one_jumps*three_jumps)
