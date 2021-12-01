import os
file = open("Day2Input.txt")

passwords = []
for line in file:
	passwords.append(line)
valid = 0
for entry in passwords:
	policy, password = entry.split(':')
	bounds, letter = policy.split(' ')
	bot, top = bounds.split('-')

	firstCheck = (password[int(bot)] == letter)
	secondCheck = (password[int(top)] == letter)
	
	if firstCheck and not secondCheck:
		valid += 1
	elif secondCheck and not firstCheck:
		valid += 1
print valid