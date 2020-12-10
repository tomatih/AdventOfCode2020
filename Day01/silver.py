#!/usr/bin/env python

def binary_search(data, num):
	start = 0
	end = len(data)-1
	while start <= end:
		needle = (start+end)//2
		stabbed = data[needle] +num
		if stabbed == 2020:
			return True,data[needle]
		elif stabbed > 2020:
			end = needle - 1
		else:
			start = needle + 1
	return False,-1


with open("input.txt") as f:
	data = [int(x) for x in f.readlines()]

data.sort()

for num in data:
	found, other = binary_search(data, num)
	if found:
		print(other*num)
		break
