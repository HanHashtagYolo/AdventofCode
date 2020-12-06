import os
import string

file = open("Day6Input.txt")

groupAnswers = {}
i = 0
groupAnswers[0] = []
for line in file:
	line = line.strip('\n')
	if len(line) == 0:
		i += 1
		groupAnswers[i] = []
	else:
		groupAnswers[i].append(line)

sumCnts = 0
for i in range(len(groupAnswers)):
	groupCnt = 0
	curGroup = groupAnswers[i]
	for letter in string.lowercase:
		if all(letter in person for person in curGroup):
			groupCnt += 1
	sumCnts += groupCnt
print sumCnts
