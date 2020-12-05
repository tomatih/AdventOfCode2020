#!/usr/bin/env python
import re

out = 0

def hight_check(a):
	if a[-2:] == "cm":
		return 150<=int(a[:-2])<=193
	elif a[-2:] == "in":
		return 59<=int(a[:-2])<=76
	return False

req_fields = {
	"byr": lambda a: 1920<=int(a)<=2002,
	"iyr": lambda a: 2010<=int(a)<=2020,
	"eyr": lambda a: 2020<=int(a)<=2030,
	"hgt": hight_check,
	"hcl": lambda a: re.match(r"#[0-9a-f]{6}",a) != None,
	"ecl": lambda a: a in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
	#"pid": lambda a: re.match(r"[0-9]{9}",a) != None
	"pid": lambda a: len(a)==9 and int(a)>=0
}
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
				if key in req_fields and req_fields[key](val):
					check+=1

print(out)