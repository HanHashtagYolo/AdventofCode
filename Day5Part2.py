import os
file = open("Day5Input.txt")
seatIDs = []
for line in file:
	line = line.strip('\n')
	rows = range(128)
	seats = range(8)
	rowString = line[:7]
	seatString = line[7:]

	for split in rowString:
		cutOff = len(rows)//2
		if split == 'F':
			rows = rows[:cutOff]
		else:
			rows = rows[cutOff:]
	row = rows[0]
	for split in seatString:
		cutOff = len(seats)//2
		if split == 'R':
			seats = seats[cutOff:]
		else:
			seats = seats[:cutOff]
	seat = seats[0]
		
	seatID = (row * 8) + seat
	seatIDs.append(seatID)

mySeat = 0
for seatID in seatIDs:
	lowest  = seatID-2
	low     = seatID-1
	highest = seatID+2
	high    = seatID+1
	if lowest in seatIDs and not low in seatIDs:
		mySeat = low
	if highest in seatIDs and not high in seatIDs:
		mySeat = high
print mySeat
