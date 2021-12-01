import os
def checkOccupied(y, x, seats):
	occupiedSeats = 0
	if y-1>=0: 
		if x-1>=0:
			if seats[y-1][x-1] == '#':
				occupiedSeats += 1
		if x+1<=(len(seats[0])-1):
			if seats[y-1][x+1] == '#':
				occupiedSeats += 1
		if seats[y-1][x] == '#':
			occupiedSeats += 1
	if y+1<= (len(seats)-1):
		if x-1>=0:
			if seats[y+1][x-1] == '#':
				occupiedSeats += 1
		if x+1<=(len(seats[0])-1):
			if seats[y+1][x+1] == '#':
				occupiedSeats += 1
		if seats[y+1][x] == '#':
			occupiedSeats += 1
	if x-1>=0:
		if seats[y][x-1] == '#':
			occupiedSeats += 1
	if x+1<=len(seats[0])-1:
		if seats[y][x+1] == '#':
			occupiedSeats += 1
	return occupiedSeats

file = open('Day11Input.txt')			
seats = {}
lineCnt = 0
for line in file:
	line=line.strip()
	a = []
	for ch in line:
		a.append(ch)
	seats[lineCnt] = a
	lineCnt += 1

changesMade = True
while changesMade is not False:
	changesMade = False
	nextSeats = {}
	for y in range(len(seats)):
		newRow = []
		for x in range(len(seats[0])):
			occupiedSeats = 0
			if seats[y][x] == '.':
				newRow.append('.')
			elif seats[y][x] == 'L':
				occupiedSeats = checkOccupied(y, x, seats)
				if occupiedSeats == 0:
					newRow.append("#")
					changesMade = True
				else:
					newRow.append("L")
			elif seats[y][x] == '#':
				occupiedSeats = checkOccupied(y, x, seats)
				if occupiedSeats >= 4:
					newRow.append("L")
					changesMade = True
				else:
					newRow.append("#")
		nextSeats[y] = newRow
	seats = nextSeats
endOccupied = 0
for line in seats:
	for z in seats[line]:
		if z == '#':
			endOccupied += 1
print endOccupied


