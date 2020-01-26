"""
Supreme Court

Write a program that requests a president then prints out the justices that served under them.
"""

def main():
	file = "Justices.txt"
	presidents(file)
	getData(file)

def presidents(file):
	infile = open(file, 'r')
	presidents = [line.rstrip().split(',')[2] for line in infile]
	infile.close()
	print()

	for president in presidents:
		print(president)

def getData(file):
	infile = open(file, 'r')
	justices = [line.rstrip().split(',') for line in infile]
	infile.close()

	for i in range(len(justices)):
		justices[i][4] = eval(justices[i][4])
		justices[i][5] = eval(justices[i][5])

	print()
	president = input("Enter the name of a president: ")
	print()

	print("Justices Appointed: ")
	for item in justices:
		if item[2] == president:
			print("  " + item[0] + " " + item[1])

main()