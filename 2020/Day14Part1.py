import os

def convertToBin(value):
	binary = str(bin(value))[2:]
	a = ''
	for i in range(0, 36-len(binary)):
		a +='0'
	return a+binary

def convertToInt(binStr):
	binStr + '0b' + binStr
	value = int(binStr,2)
	return value

file = open("Day14Input.txt")
mask=''
mem = {}
for line in file:
	line = line.strip()
	if line.startswith("mask"):
		mask = line.split('=')[1].strip()
	else:
		memAddr, value = line.split('=')
		memAddr = memAddr.strip()[4:-1]
		value = int(value.strip())
		binary = convertToBin(value)
		tempMem = ''
		for i in range(0,len(binary)):
			#print mask[i], binary[i]
			if mask[i] == "X":
				tempMem += binary[i]
			else:
				tempMem += mask[i]
		newValue = convertToInt(tempMem)

		mem[memAddr] = newValue
a = 0
for entry in mem:
	a += mem[entry]
print a