# Assignment 5: Message Frequency Count
# Student: Anthony Sim


fhand = open('mbox.txt')

counts = dict()
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:'):
		continue
	
	atpos = line.find(' ')
	emails = line[atpos + 1: ]

	if emails not in counts:
		counts[emails] = 1
	else:
		counts[emails] += 1

lst = list()
for key, val in list(counts.items()):
	lst.append((val, key))

lst.sort(reverse = True)

for key, val in lst[:1]:
	print(key, val)