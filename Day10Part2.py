import os

file = open("Day10Input.txt")

adapters = []
for line in file:
	adapters.append(int(line.strip()))

adapters.sort()
adapters.insert(0,0)
branches = {}
branches[adapters[len(adapters)-1]] = 1
i = len(adapters) - 2
while i >= 0:
	joltage = adapters[i]
	branches[joltage] = 0
	if (joltage + 1) in adapters:
		branches[joltage] = branches[joltage] + branches[joltage +1]
	if (joltage + 2) in adapters:
		branches[joltage] = branches[joltage] + branches[joltage +2]
	if (joltage + 3) in adapters:
		branches[joltage] = branches[joltage] + branches[joltage +3]
	i-=1
print branches[0]