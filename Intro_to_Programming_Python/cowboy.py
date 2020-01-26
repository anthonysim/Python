"""
Cowboy

A program that takes whats in Cowboy.txt and makes a new file with the same info. 
"""

def main():
	cowboys = getData("Cowboy.txt")

	outfile = open("Cowboy2.txt", 'w')
	
	createFile(cowboys, outfile)

def getData(f):
	infile = open(f, 'r')
	cowboys = [line.rstrip() for line in infile]	
	infile.close()

	return cowboys

def createFile(cowboys, outfile):
	for i in range(len(cowboys)):
		cowboys[i] = cowboys[i] + "\n"
	outfile.writelines(cowboys)
	outfile.close()

main()