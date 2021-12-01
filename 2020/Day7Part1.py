import os

def checkForGold(startBag, rules):
#is shiny gold in the bag? if so return true otherwise check the next bag
	goldBagExists = False
	if "shiny gold" in rules[startBag]:
		return True
	else:
		for bag in rules[startBag]:
			if rules[bag] != None:
				goldBagExists = checkForGold(bag, rules)
				if goldBagExists:
					break
	return goldBagExists
		
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

goldCnt = 0
for bagColor in rules:
	if rules[bagColor] != None:
		hasGold = checkForGold(bagColor, rules)
		if hasGold:
			goldCnt+=1
print goldCnt


