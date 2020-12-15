#!/usr/bin/env python

with open("input.txt") as f:
    num_list = [int(x) for x in f.read().strip().split(",")]


turn_number = 0
last_spoken = None
memory = dict()


def speak(num):
    global last_spoken, turn_number, memory
    if num in memory:
        memory[num] = [turn_number] + memory[num][:-1]
    else:
        memory[num] = [turn_number, None]
    last_spoken = num
    turn_number += 1
    # print("turn:",turn_number,"spoken:",num)


def play_game():
    global turn_number, last_spoken
    if turn_number < len(num_list):
        speak(num_list[turn_number])
    else:
        if (not last_spoken in memory) or memory[last_spoken][1] == None:
            speak(0)
        else:
            speak(memory[last_spoken][0]-memory[last_spoken][1])


# execution time 72.3s
for i in range(30000000):
    play_game()
print(last_spoken)
