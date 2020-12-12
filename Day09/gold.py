#!/usr/bin/env python

memory = list()
accumulator = 0
target = 85848519
#target = 127

with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        val = int(line)
        memory.append(val)
        accumulator += val
        if accumulator == target:
            print(min(memory)+max(memory))
            quit()
        while accumulator > target:
            accumulator -= memory[0]
            memory = memory[1:]
            if accumulator == target:
                print(min(memory)+max(memory))
                quit()
