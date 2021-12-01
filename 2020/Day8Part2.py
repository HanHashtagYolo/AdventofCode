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


for entry in code:
	print code[entry]
	if 'nop' in code[entry]:
		code[entry]=code[entry].replace('nop','jmp')
	elif 'jmp' in code[entry]:
		code[entry]=code[entry].replace('jmp','nop')
	print code[entry]
	location = 0
	count = 0
	executedOps = []
	secondTime = False
	try:
		while secondTime is not True:
			if location in executedOps:
				#print location
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
	except:
		print count
		break
	if 'nop' in code[entry]:
		code[entry]=code[entry].replace('nop','jmp')
	elif 'jmp' in code[entry]:
		code[entry]=code[entry].replace('jmp','nop')