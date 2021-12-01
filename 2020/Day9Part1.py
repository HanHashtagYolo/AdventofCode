import os

def findWeakness(target, parts):
	done = False
	for i in range(0,len(parts)):
		startNum = total = parts[i]
		y = i+1
		currentNumbers = [startNum]
		while total < target:
			currentNumbers.append(parts[y])
			total += parts[y]
			if total == target:
				endNum = parts[y]
				done = True
				break
			y +=1
		if done:
			break
	currentNumbers.sort()
	print currentNumbers[0] + currentNumbers[-1]

file = open("Day9Input.txt")
numbers = []
for line in file:
	numbers.append(int(line.strip()))
for i in range(25,len(numbers)):
	notMissing = False
	check = numbers[i-25:i]
	data = numbers[i]
	for entry in check:
		temp = data - entry
		if temp in check:
			notMissing = True
	if not notMissing:
		badNum = numbers[i]
		break
print badNum
findWeakness(badNum, numbers[:i])