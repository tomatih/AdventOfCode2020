#!/usr/bin/env python

out = 0

with open("input.txt") as f:
	for line in f.readlines():
		rule, pasw = line.split(": ")
		nums, target = rule.split(" ")
		low, high = [int(x)-1 for x in nums.split("-")]
		if (pasw[low]==target) ^ (pasw[high]==target):
			out+=1
print(out)