# Assignment 3 - Looping, Searching, & Slicing
# File: process_numbers.py
# Student: Anthony Sim

# print count, max, min, average 

count = 0
total = 0
largest = None
smallest = None

while True:
	number = input("Please type in a number: ")
	
	if number == '':
		print("I SAID type in a number, if you're finished typed in 'done!'")
		continue
	
	if number == 'done':
		break

	count += 1
	total += int(number)

	if largest == None or number > largest:
		largest = number

	if smallest == None or number < smallest:
		smallest = number

print()
print('Total:', total)	
print('Count:', count)
print('Maximum:', largest)
print('Minimum:', smallest)
print('Average:', (total / count))