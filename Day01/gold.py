#!/usr/bin/env python


def binary_search(data, num):
    start = 0
    end = len(data)-1
    while start <= end:
        needle = (start+end)//2
        stabbed = data[needle] + num
        if stabbed == 2020:
            return True, data[needle]
        elif stabbed > 2020:
            end = needle - 1
        else:
            start = needle + 1
    return False, -1


with open("input.txt") as f:
    data = [int(x) for x in f.readlines()]

data.sort()

for num1 in data:
    for num2 in data:
        found, num3 = binary_search(data, num1+num2)
        if found:
            print(num1*num2*num3)
            quit()
