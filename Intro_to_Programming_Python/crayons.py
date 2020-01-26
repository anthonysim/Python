""" Crayon Colors

Remove the 8 colors in "Retired.txt" from "pre1990.txt" then add the 56 new colors from "Added.txt."
Add the new updated list of colors to a file called "updated.txt"
"""

def main():
	listPre = pre1990("Pre1990.txt")
	listRet = retired("Retired.txt")
	listAdd = added("Added.txt")
	listUpdated = update(listPre, listRet, listAdd)
	colors(listUpdated)

def pre1990(file):
	infile = open(file, 'r')
	listPre = [line.rstrip() for line in infile]
	infile.close()
	return listPre

def retired(file):
	infile = open(file, 'r')
	listRet = [line.rstrip() for line in infile]
	infile.close()
	return listRet

def added(file):
	infile = open(file, 'r')
	listAdd = [line.rstrip() for line in infile]
	infile.close()
	return listAdd

def update(listPre, listRet, listAdd):
	remaining = set(listPre).difference(listRet)
	listUpdated = set(remaining).union(listAdd)
	listUpdated = list(listUpdated)
	return listUpdated

def colors(listUpdated):
	listUpdated.sort()
	for i in range(len(listUpdated)):
		listUpdated[i] = listUpdated[i] + "\n"
	outfile = open("updated.txt", 'w')
	outfile.writelines(listUpdated)
	outfile.close()

main()