"""
Dogs of Dow

Top 10 Dow Stocks w/ the highest ratios of dividends in 2013.
Use DOW.txt file
"""

def main():
	print()
	file = "DOW.txt"
	dowData = getData(file)
	top10 = divRatios(dowData)
	top10.sort(key=lambda top10: top10[2], reverse=True)
	results(top10)

def getData(file):
	infile = open(file, 'r')
	dowData = [line.rstrip().split(',') for line in infile]
	infile.close()

	for i in range(len(dowData)):
		dowData[i][4] = eval(dowData[i][4])
		dowData[i][5] = eval(dowData[i][5])
		dowData[i][6] = eval(dowData[i][6])
		dowData[i][7] = eval(dowData[i][7])
	return dowData

def divRatios(dowData):	
	top10 = []
	for item in dowData:
		ratios = (item[0], item[1], item[-1] / item[5] * 100)
		top10.append(list(ratios))
	return top10

def results(top10):
	print("{0:20} {1:15} {2:20}".format("Company", "Symbol", "Yield as of 12/31/2013"))

	for i in range(10):
		print("{0:20} {1:15} {2:,.2f}%".format(top10[i][0], top10[i][1], top10[i][2]))

main()
