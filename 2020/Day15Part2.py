import os

startNums = [1,20,8,12,0,14]

numTurns = 30000000
startTurn = len(startNums)
numLastPos = {}
checkNum = startNums[-1]
for num in startNums:
	numLastPos[num] = startNums.index(num)

for i in range(startTurn, numTurns):
	previousNum = checkNum
	if previousNum not in numLastPos:
		checkNum = 0
		numLastPos[previousNum] = i-1
	else:
		checkNum = i - 1 - numLastPos[previousNum]
		numLastPos[previousNum] = i-1
print checkNum