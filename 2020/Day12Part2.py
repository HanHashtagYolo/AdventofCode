import os

file = open("Day12Input.txt")

moves = []
for line in file:
	moves.append(line.strip())

cardinals = ['W','N','E','S']
yAxis = 0
xAxis = 0
waypointX = 10
waypointY = 1
for move in moves:
	command = move[0]
	value = int(move[1:])
	if command == 'L' or command == 'R':
		ticks = value/90
		if ticks%2 == 0:
			waypointX = waypointX*-1
			waypointY = waypointY*-1
		else:
			tempX = 0
			tempY = 0
			if value == 90:
				if command == 'L':
					tempY = waypointX
					tempX = -1*waypointY
				else:
					tempY = -1*waypointX
					tempX = waypointY
			else:
				if command == 'L':
					tempY = -1*waypointX
					tempX = waypointY
				else:
					tempY = waypointX
					tempX = -1*waypointY
			waypointX = tempX
			waypointY = tempY
	if command == 'N':
		waypointY += value
	if command == 'E':
		waypointX += value
	if command == 'S':
		waypointY -= value
	if command == 'W':
		waypointX -= value
	if command == 'F':
		yAxis += waypointY * value
		xAxis += waypointX * value
print abs(yAxis) + abs(xAxis)