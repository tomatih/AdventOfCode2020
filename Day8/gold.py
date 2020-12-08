#!/usr/bin/env python

class interpreter:

	def  __init__(self):
		self.accumultaor = 0
		self.cursor = 0
		self.instructions = list()
		self.instruction_set = {
			"acc": self.acc,
			"jmp": self.jmp,
			"nop": lambda a: None
		}
		self.used = list()

	def load_instructions(self):
		with open("input.txt") as f:
			for line in f.readlines():
				line = line.strip()
				instr, val = line.split(" ")
				val = int(val)
				self.instructions.append([instr,val])

	def run(self):
		while 1:
			# exit conditions
			if self.cursor in self.used:
				return False
			if self.cursor == len(self.instructions):
				print(self.accumultaor)
				return True
			if self.cursor > len(self.instructions):
				return False
			# load data
			self.used.append(self.cursor)
			instr, val = self.instructions[self.cursor]
			# execute
			# print("doing: ",instr,val, "at", self.cursor)
			self.instruction_set[instr](val)
			# move cursor
			self.cursor += 1

	# instruction definitions
	def acc(self, val):
		self.accumultaor += val

	def jmp(self, val):
		self.cursor += val-1

	# day specific functions
	def change_instruction(self, i):
		if self.instructions[i][0] == "nop":
			self.instructions[i][0] = "jmp"
		elif self.instructions[i][0] == "jmp":
			self.instructions[i][0] = "nop"

	def run_test(self):
		for i in range(len(self.instructions)):
			self.change_instruction(i)
			self.accumultaor = 0
			self.cursor = 0
			self.used = list()
			if self.run():
				return
			self.change_instruction(i)

if __name__ == '__main__':
	intr = interpreter()
	intr.load_instructions()
	intr.run_test()