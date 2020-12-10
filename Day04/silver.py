#!/usr/bin/env python

out = 0
req_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
check = 0

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		if len(line)==0:
			#end of passport
			out+= 1 if check==len(req_fields) else 0
			check = 0
		else:
			#get data
			pairs = line.split(" ")
			for pair in pairs:
				key, val = pair.split(":")
				if key in req_fields:
					check+=1

print(out)