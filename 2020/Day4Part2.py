import os

def PassportCheck(fields):
	isValid = True
	eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	for field in fields:
		key, value = field.split(':')
		print key, value
		if key == 'byr':
			year = int(value)
			if len(value) != 4:
				isValid = False
				break
			if year < 1920 or year > 2002:
				isValid = False
				break
		if key == 'iyr':
			year = int(value)
			if len(value) != 4:
				isValid = False
				break
			if year < 2010 or year > 2020:
				isValid = False
				break
		if key == 'eyr':
			year = int(value)
			if len(value) != 4:
				isValid = False
				break
			if year < 2020 or year > 2030:
				isValid = False
				break
		if key == 'hgt':
			measure = value[-2:]
			if measure != 'cm' and measure != 'in':
				isValid = False
				break
			height = int(value[:-2])
			if measure == 'cm':
				if height < 150 or height > 193:
					isValid = False
					break
			if measure == 'in':
				if height < 59 or height > 76:
					isValid = False
					break
		if key == 'hcl':
			if len(value) != 7:
				isValid = False
				break
			if value[0] != '#':
				isValid = False
				break
			if len(value[1:]) != 6:
				isValid = False
				break
			if not all(c in '0123456789abcdef' for c in value[1:]):
				isValid = False
				break
		if key == 'ecl':
			if value not in eyeColors:
				isValid = False
				break
		if key == 'pid':
			if len(value) != 9:
				isValid = False
				break
			if not all(c in '0123456789' for c in value):
				isValid = False
				break

	return isValid


file = open('Day4Input.txt')

i = 0
passports = []
tempPass = ''
for line in file:
	line = line.strip('\n')
	if len(line) == 0:
		passports.append(tempPass)
		tempPass = ''
		continue
	else:
		if len(tempPass) == 0:
			tempPass = line
		else:
			tempPass = tempPass + ' ' + line
#append last line
if len(line) != 0:
	passports.append(tempPass)
print passports[-2] , len(passports[-2])

valid = 0

for passport in passports:
	fields = passport.split(' ')
	if len(fields) == 8:
		isValid = PassportCheck(fields)
		if isValid:
			valid += 1
	elif len(fields) == 7:
		cidPresent = False
		for field in fields:
			key, value = field.split(':')
			if key == 'cid':
				cidPresent = True
				break
		if not cidPresent:
			isValid = PassportCheck(fields)
			if isValid:
				valid += 1
print valid