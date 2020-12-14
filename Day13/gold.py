#!/usr/bin/env python
# from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# my code
with open("input.txt") as f:
    _, busses = f.read().strip().split("\n")

busses = busses.split(",")
n = list()
a = list()

for i in range(len(busses)):
    if busses[i] != "x":
        bid = int(busses[i])
        pos = i % bid if i % bid != 0 else bid
        # M *=bid
        n.append(bid)
        a.append(-pos+bid)
        # busses_calc.append((bid,-pos+bid)) # divider,reminder n,a
print(chinese_remainder(n, a))
