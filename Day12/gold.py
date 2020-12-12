#!/usr/bin/env python

from dataclasses import dataclass

@dataclass
class Point:
	x: int
	y: int

	def __add__(self, other):
		tmp = Point(self.x,self.y)
		tmp.x += other.x
		tmp.y += other.y
		return tmp

	def __mul__(self,other:float):
		tmp = Point(self.x,self.y)
		tmp.x *= other
		tmp.y *= other
		return tmp


class Ship:

	def __init__(self):
		self.pos = Point(0,0) # true point
		self.way = Point(10,1) # vector
		self.pos_mod = {
			"N":Point(0,1),
			"E":Point(1,0),
			"S":Point(0,-1),
			"W":Point(-1,0)
		}

	def move(self,direction,amount):
		if direction in "NESW":
			self.way += self.pos_mod[direction]*amount
		elif direction in "RL":
			# ensure angle counterclockwise
			if direction == "R":
				amount = abs(amount-360)
			# rotate 
			if amount == 90:
				self.way.x, self.way.y = -self.way.y, self.way.x
			elif amount == 180:
				self.way *= -1
			elif amount == 270:
				self.way.x, self.way.y = self.way.y, -self.way.x
		elif direction == "F":
			self.pos += self.way * amount

	def __repr__(self):
		return str(abs(self.pos.x)+abs(self.pos.y))


ship = Ship()

with open("input.txt") as f:
	for line in f.readlines():
		ship.move(line[0],int(line[1:]))

print(ship)




