#!/usr/bin/env python


class interpreter:

    def __init__(self):
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
                self.instructions.append((instr, val))

    def run(self):
        while 1:
            if self.cursor in self.used:
                print(self.accumultaor)
                break
            self.used.append(self.cursor)
            instr, val = self.instructions[self.cursor]
            self.instruction_set[instr](val)
            self.cursor += 1

    def acc(self, val):
        self.accumultaor += val

    def jmp(self, val):
        self.cursor += val-1


if __name__ == '__main__':
    intr = interpreter()
    intr.load_instructions()
    intr.run()
