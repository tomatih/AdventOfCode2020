#!/usr/bin/env python

board = list()

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		dat= list()
		for char in line:
			if char == "L":
				dat.append(0)
			elif char == "#":
				dat.append(1)
			else:
				dat.append(-1)
		board.append(dat)

def print_board():
	trans = {0:"L",1:"#",-1:"."}
	for line in board:
		for val in line:
			print(trans[val],end="")
		print()
			
while 1:
	temp_b = list()
	changes = 0
	for i in range(len(board)):
		temp_b.append(list())
		for j in range(len(board[i])):
			# skip blank
			if board[i][j] == -1:
				temp_b[i].append(-1)
				continue
			occupied_around = 0
			# check adjecent
			for k in range(-1,2):
				# board clipping safe
				if i+k < 0 or i+k >= len(board):
					continue
				for m in range(-1,2):
					# clippig safe
					if j+m < 0 or j+m >=len(board[i+k]):
						continue
					# ignore self
					if m==0 and k==0:
						continue
					# check seat
					if board[i+k][j+m] == 1:
						occupied_around += 1
					elif board[i+k][j+m] == -1:
						n = 2
						while 1:
							# clippig safe
							if j+(m*n) < 0 or j+(m*n) >=len(board[i+k]):
								break
							if i+(k*n) < 0 or i+(n*k) >= len(board):
								break
							# cheks
							if board[i+(k*n)][j+(m*n)] == 1:
								occupied_around+=1
								break
							elif board[i+(k*n)][j+(m*n)] == 0:
								break
							else:
								n+=1

							

			# act according to rules
			if board[i][j] == 0 and occupied_around == 0:
				temp_b[i].append(1)
				changes+=1
			elif board[i][j] == 0:
				temp_b[i].append(0)
			elif board[i][j] == 1 and occupied_around >= 5:
				temp_b[i].append(0)
				changes+=1
			elif board[i][j] == 1:
				temp_b[i].append(1)
	board = temp_b
	if changes == 0:
		break

# count occupied
out = 0
for line in board:
	out += line.count(1)

print(out)
#print_board()
