import os

file = open("Day10Input.txt")

adapters = []
for line in file:
	adapters.append(int(line.strip()))

adapters.sort()
oneCount = 1
threeCount = 1

for i in range(len(adapters)-1):
	joltDiff = adapters[i+1] - adapters[i]
	if joltDiff == 1:
		oneCount += 1
	elif joltDiff == 3:
		threeCount += 1


print oneCount * threeCount