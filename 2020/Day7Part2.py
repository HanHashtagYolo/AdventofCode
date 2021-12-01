import os

def getBagCount(startColor, rules):
#if
	bagCnt = 0
	bagSet = rules[startColor]
	for color in bagSet:
		if rules[color] != None:
			count = int(bagSet[color])
			bagCnt += ( count + count * getBagCount(color, rules))
		else:
			bagCnt += int(bagSet[color])
	return bagCnt

	return
		
file = open("Day7Input.txt")

rules = {}
for line in file:
	line.strip()
	inBags = []
	outBag, tempBags = line.split("contain")
	outBag = outBag.replace("bags", "").strip()
	rules[outBag] = {}
	inBags = tempBags.split(',')
	for item in inBags:
		if 'no other' not in item:
			item = item.strip()
			itemSplit = item.split(' ')
			bagCnt = itemSplit[0]
			color = itemSplit[1] + ' ' + itemSplit[2]
			rules[outBag][color] = bagCnt
		else:
			rules[outBag] = None

goldBagCnt = 0
goldBagCnt = getBagCount('shiny gold', rules)
print goldBagCnt