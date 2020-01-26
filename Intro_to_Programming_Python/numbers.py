"""
Largest Number & Sum of Numbers

Display the largest and sum of numbers
"""

def main():
	file = "Numbers.txt"
	max, total = numbers(file)

	results(max, total)

def numbers(file):
	infile = open(file, 'r')
	numbers = [line.rstrip() for line in infile]
	numbers.sort()
	
	max = numbers[-1]

	total = 0
	for number in numbers:
		total += int(number)

	return max, total

def results(max, total):
	print("Your maximum number is:\t", max)
	print("Your total is:\t\t", total)

main()
