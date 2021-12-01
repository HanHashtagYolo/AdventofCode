import os

file = open("Day12Input.txt")

moves = []
for line in file:
	moves.append(line.strip())

cardinals = ['W','N','E','S']
yAxis = 0
xAxis = 0
facing = 'E'
for move in moves:
	command = move[0]
	value = move[1:]
	if command == 'L' or command == 'R':
		ticks = int(value)/90
		index = cardinals.index(facing)
		if command == 'L':
			facing = cardinals[index-ticks]
		if command == 'R':
			facing = cardinals[(index+ticks)%4]
	elif command == 'F':
		if facing == 'E':
			xAxis += int(value)
		if facing == 'W':
			xAxis -= int(value)
		if facing == 'N':
			yAxis += int(value)
		if facing == 'S':
			yAxis -= int(value)
	if command in cardinals:
		if command == 'E':
			xAxis += int(value)
		if command == 'W':
			xAxis -= int(value)
		if command == 'N':
			yAxis += int(value)
		if command == 'S':
			yAxis -= int(value)
print abs(yAxis) + abs(xAxis)