"""
DOW

1) Program listing the 30 DOW stocks in alpha order.
2) Asks for symbol then lists the company, industry, exchange, growth in 2013
and price/earning ratio in 2013.

Use DOW.txt file. Lists name, symbol, exchange, industry, price as of 12/31/2012 and price as of 12/31/2013,
2013 earnings per share, and dividend paid in 2013.
"""

def main():
	print()
	file = "DOW.txt"
	getSymbols(file)
	print()
	getInfo(file)

def getSymbols(file):
	print("Symbols for the Thirty DOW Stocks:")
	infile = open(file, 'r')
	dowSymbols = [line.rstrip().split(',')[1] for line in infile]
	infile.close()

	i = 0
	while i < 10:
		print(str(dowSymbols[i]) +"\t", end=' ')
		i += 1
	print()
	while i < 20:
		print(str(dowSymbols[i]) +"\t", end=' ')
		i += 1
	print()
	while i < 30:
		print(str(dowSymbols[i]) +"\t", end=' ')
		i += 1
	print()	

def getInfo(file):
	infile = open(file, 'r')
	fullList = [line.rstrip().split(',') for line in infile]
	infile.close()

	symbol = str(input("Enter a symbol: "))

	for item in fullList:
		if item[1] == symbol:
			item[4] = eval(item[4])
			item[5] = eval(item[5])
			item[6] = eval(item[6])
			item[7] = eval(item[7])

			print("Company:", item[0])
			print("Industry:", item[3])
			print("Exchange:", item[2])
			print("Growth in 2013: {0:,.2f}%".format(((item[5] - item[4]) / item[4]) * 100))
			print("Price/Earnings ratio in 2013: {0:,.2f}".format(item[5] / item[6]))

main()
