import os

def checkOccupied(y, x, seats):
	directions = {
		0 : [-1, -1],
		1 : [0 , -1],
		2 : [1 , -1],
		3 : [-1,  0],
		4 : [1 ,  0],
		5 : [-1 , 1],
		6 : [0 ,  1],
		7 : [1 ,  1],
	}
	occupiedSeats = 0
	for point in directions:
		deltX = directions[point][0]
		deltY = directions[point][1]
		tempX = x
		tempY = y
		hitSeat = False
		while hitSeat == False:
			if tempY + deltY >=0 and tempY+deltY<=(len(seats)-1) and tempX + deltX >=0 and tempX+deltX<=(len(seats[0])-1): 
				tempX += deltX
				tempY += deltY
				if seats[tempY][tempX] == 'L':
					hitSeat = True
				elif seats[tempY][tempX] == '#':
					occupiedSeats += 1
					hitSeat = True
			else:
				hitSeat = True
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
				if occupiedSeats >= 5:
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