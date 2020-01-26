"""
2015 Calendar

1) Use Excel to create a spreadsheet of 365 rows and 2 columns listing the date and day for 2015.
2) Save the spreadsheet as a CSV file named Calendar2015.csv.
3) Change the name of the file to a txt.
4) Use the tex file in a program that requests a date in 2015 as input and then gives its day
of the week.
"""

def main():
	print()
	date = input("Enter a date in 2015: ")
	getData("Calendar2015.txt", date)

def getData(f, date):
	infile = open(f, 'r')
	calendar = [line.rstrip().split(',') for line in infile]
	infile.close()

	for i in range(len(calendar)):
		if calendar[i][0] == date:
			print(date, "falls on a", calendar[i][1])
		else:
			pass

main()