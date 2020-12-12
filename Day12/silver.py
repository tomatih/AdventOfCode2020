#!/usr/bin/env python

from dataclasses import dataclass

@dataclass
class Point:
	x: int
	y: int

	def __add__(self, other):
		tmp = Point(0,0)
		tmp.x += self.x
		tmp.x += other.x
		tmp.y += self.y
		tmp.y += other.y
		return tmp

	def __mul__(self,other):
		tmp = Point(0,0)
		tmp += self
		tmp.x *= other
		tmp.y *= other
		return tmp


class Ship:

	def __init__(self):
		self.pos = Point(0,0)
		self.rot = 0
		self.rot_mod = {
			0 : Point(1,0),
			90: Point(0,1),
			180:Point(-1,0),
			270:Point(0,-1) 
		}
		self.pos_mod = {
			"N":Point(0,1),
			"E":Point(1,0),
			"S":Point(0,-1),
			"W":Point(-1,0)
		}

	def move(self,direction,amount):
		if direction in "NESW":
			self.pos += self.pos_mod[direction]*amount
		elif direction in "RL":
			self.rot += amount * (1 if direction=="L" else -1)
			if self.rot >= 360:
				self.rot -= 360
			if self.rot < 0:
				self.rot += 360
		elif direction == "F":
			self.pos += self.rot_mod[self.rot] * amount

	def __repr__(self):
		return str(abs(self.pos.x)+abs(self.pos.y))


ship = Ship()

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		ship.move(line[0],int(line[1:]))

print(ship)




