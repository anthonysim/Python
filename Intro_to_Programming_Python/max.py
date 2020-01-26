""" 
Max Function

A function that asks for a list of numbers then determines the maximum number from that list. 
"""

def main():
	max_number = max()
	print("Your maximum number is:", max_number)

def max():
	count = int(input("How many numbers in your list?: "))
	numbers = []

	for number in range(count):
		number = int(input("Enter a number: "))
		numbers.append(number)
	numbers.sort()
	max_number = numbers[-1]
	return max_number

main()
