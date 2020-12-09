import os

file = open("Day8Input.txt")

count = 0
executedOps = []
code = {}
secondTime = False
i = 0
for line in file:
	line = line.strip()
	code[i] = line
	i += 1

location = 0
while secondTime is not True:
	print code[location]
	if location in executedOps:
		secondTime = True
		continue
	executedOps.append(location)
	op, arg = code[location].split(" ")	
	arg = int(arg)
	if op == 'nop':
		location += 1
	elif op == 'acc':
		count += arg
		location += 1
	elif op == 'jmp':
		location += arg
	print count
	print executedOps
print count