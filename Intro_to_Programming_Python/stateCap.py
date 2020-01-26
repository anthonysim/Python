"""
State Capitals

A program that displays the states (and their capitals) for which
the name of the state and its capital begin with the same letter.
Use StatesANC.txt
"""

def main():
	file = "StatesANC.txt"
	getData(file)

def getData(file):
	infile = open(file, 'r') 
	states = [line.rstrip().split(',') for line in infile]
	infile.close()

	for state in states:
		# print(state[3][0], state[0][0])
		if state [3][0] == state[0][0]:
			print(str(state[3]) + ", " + str(state[0]))
		else:
			pass

main()
