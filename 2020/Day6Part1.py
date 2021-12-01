import os
import string

file = open("Day6Input.txt")

groupAnswers = []
tempGroup = ''
for line in file:
	line = line.strip('\n')
	if len(line) == 0:
		groupAnswers.append(tempGroup)
		tempGroup = ''
		continue
	else:
		tempGroup += line
if len(line) != 0:
	groupAnswers.append(tempGroup)

totalYes = 0
for group in groupAnswers:
	for letter in string.lowercase:
		if letter in group:
			totalYes += 1

print totalYes