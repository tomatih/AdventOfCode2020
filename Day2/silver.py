#!/usr/bin/env python

out = 0

with open("input.txt") as f:
	for line in f.readlines():
		rule, pasw = line.split(": ")
		nums, target = rule.split(" ")
		low, high = [int(x) for x in nums.split("-")]
		accumulator = 0
		for letter in pasw.strip():
			if letter == target:
				accumulator+=1
		if low <= accumulator <= high:
			out+=1

print(out)