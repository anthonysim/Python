""" 
Min Function

A function that returns the minimum value in a list of numbers.
"""

def main():
	min_number = min()
	print("Your minimum number is:", min_number)

def min():
	count = int(input("How many numbers in your list?: "))
	numbers = []

	for number in range(count):
		number = int(input("Enter a number: "))
		numbers.append(number)
	numbers.sort()
	min_number = numbers[0]
	return min_number

main()

