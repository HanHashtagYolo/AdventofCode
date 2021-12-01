import os
from collections import OrderedDict
file = open('Day13Input.txt')
busses = OrderedDict()
for line in file:
	line = line.strip()
	if ',' in line:
		temp = line.split(',')
		for entry in temp:
			if entry != 'x':
				busses[int(entry)] = temp.index(entry)
iterator = 0
for entry in busses:
	if busses[entry] == 0:
		iterator = entry

rightTime = False
i = 1
t = iterator
print busses
for bus in busses:
	if bus == iterator:
		continue
	else:
		checking = True
		while checking:
			if (t+busses[bus]) % int(bus) == 0:
				iterator = iterator*bus
				checking=False
			else:
				t += iterator
print t