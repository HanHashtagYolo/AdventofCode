import os

def countTrees(right, down):
	file = open("Day3Input.txt")
	hillMap = []
	for line in file:
		hillMap.append(line.strip('\n'))
	
	position = 0
	treesHit = 0
	width = len(hillMap[0])
	for i in range(0, len(hillMap),down):
		section = hillMap[i]
		if section[position] == '#':
			treesHit += 1
		position = (position + right)
		while position >= width:
			position = position - width
	return treesHit

print countTrees(3,1)
print countTrees(1,1) * countTrees(3,1) * countTrees(5,1) * countTrees(7,1) * countTrees(1,2)