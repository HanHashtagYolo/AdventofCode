import os
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
		valid += 1
	elif len(fields) == 7:
		cidPresent = False
		for field in fields:
			key, value = field.split(':')
			if key == 'cid':
				cidPresent = True
				break
		if not cidPresent:
			valid+=1
print valid
