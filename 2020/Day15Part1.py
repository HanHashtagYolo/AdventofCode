import os

startNums = [0,3,6]#[1,20,8,12,0,14]

numTurns = 2020
startTurn = len(startNums)

for i in range(startTurn+1, numTurns+1):
	if startNums[-1] not in startNums[:-1]:
		startNums.append(0)
	else:
		indices = [i for i, x in enumerate(startNums) if x == startNums[-1]]
		startNums.append(indices[-1] - indices[-2])
print startNums[numTurns-1]
	
