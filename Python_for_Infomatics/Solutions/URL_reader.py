# Assigment 6: URL Reader
# Student: Anthony Sim

import urllib.request, urllib.parse, urllib.error

website = input('Please type in a website to read: ')

try:
	fhand = urllib.request.urlopen(website)

except:
	print('Website cannot be opened:', website)
	exit()

print()

size = 0
while True:
	info = fhand.read(512)
	if (len(info) < 1): 
		break
	size += len(info)

	if size < 3000:
		print(info.decode())

print('Total number of characters:', size)
