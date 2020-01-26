"""
Colleges

A program that requests a state abbreviation as input and then displays the 
colleges in alpha order (along with their year founded) in that state. If there
are no early colleges in the state, so inform the user.
Use Colleges.txt
"""

def main():
	print()
	state = str(input("Enter a state abbreviation: "))
	state = state.upper()
	file = "Colleges.txt"

	getData(state, file)

def getData(state, file):
	infile = open(file, 'r')
	colleges = [line.rstrip().split(',') for line in infile]
	infile.close()
	
	colleges.sort()

	for college in colleges:
		if college[1] == state:
			print(college[0], college[2])
		else:
			pass

main()
