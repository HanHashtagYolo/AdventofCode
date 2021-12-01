import os
from itertools import product

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

def getMemories(maskedAddr):
	addrList = []
	xCount = maskedAddr.count("X")
	comb = list(product([0,1],repeat = xCount))
	for values in comb:
		tempAddr = maskedAddr
		for entry in values:
			tempAddr = tempAddr.replace('X', str(entry),1)
		addrList.append(convertToInt(tempAddr))
	return addrList

file = open("Day14Input.txt")
mask=''
mem = {}
for line in file:
	line = line.strip()
	if line.startswith("mask"):
		mask = line.split('=')[1].strip()
	else:
		memAddr, value = line.split('=')
		memAddr = int(memAddr.strip()[4:-1])
		value = int(value.strip())
		binaryAddr = convertToBin(memAddr)
		maskedAddr = ''
		for i in range(0,len(binaryAddr)):
			if mask[i] == 'X':
				maskedAddr += 'X'
			if mask[i] == '1':
				maskedAddr += '1'
			if mask[i] == '0':
				maskedAddr += binaryAddr[i]
		for entry in getMemories(maskedAddr):
			mem[entry] = value
a = 0
for entry in mem:
	a += mem[entry]
print a