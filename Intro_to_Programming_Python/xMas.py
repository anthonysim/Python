"""
12 Days of Christmas

1) Ask for an integer from 1 to 12
2) Lists the gifts for that day along with that day's costs
3) Give total cost up to and including that day.
Use Gifts.txt
"""

def main():
	file = "Gifts.txt"
	price = getData(file)
	print()

	days = eval(input("Enter a number from 1 through 12: "))

	dayCosts(days, price)

def getData(file):
	infile = open(file, 'r')
	price = [line.rstrip().split(',')[-1] for line in infile]
	infile.close()	

	for i in range(len(price)):
		price[i] = eval(price[i])
	
	return price

def dayCosts(days, price):
	for i in range(len(price)):
		price[i] = price[i] * (i + 1) 

	print("Cost for day " + str(days) + " days: ${0:,.2f}".format(sum(price[0: days])))

	totalCosts = 0
	for i in range(days):
		totalCosts += sum(price[:i + 1])	
	print("Total cost for the first " + str(days) + " days: ${0:,.2f}".format(totalCosts))

main()
