#!/usr/bin/env python

with open("input.txt") as f:
	time, busses = f.read().strip().split("\n")

time = int(time)
busses = [int(x) for x in busses.split(",") if x != "x"]

min_v=time
min_i=None
for i,bus in enumerate(busses):
	if bus - time%bus < min_v:
		min_v = bus - time%bus
		min_i = i

print(min_v*busses[min_i])