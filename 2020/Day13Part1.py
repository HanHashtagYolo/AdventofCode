import os

file = open('Day13Input.txt')

busses = []
startTime = 0
for line in file:
	line = line.strip()
	if ',' in line:
		temp = line.split(',')
		for entry in temp:
			if entry != 'x':
				busses.append(int(entry))
	else:
		startTime = int(line)

waitTime = 99999999999999999999
fastBus = 0
for bus in busses:
	split = startTime%bus
	tempWait = bus-split
	if tempWait < waitTime:
		waitTime = tempWait
		fastBus = bus
print waitTime * fastBus
