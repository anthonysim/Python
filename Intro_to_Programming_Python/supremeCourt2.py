"""
Supreme Court

A program that requests the name of a president as input and then
displays the names and years of the justices appointed by that president.
"""

import pickle

def main():
	dicLst = createDictFromBinaryFile("JusticesDict.dat")
	president = input("Enter a president: ")
	getJustice(dicLst, president)

def createDictFromBinaryFile(file):
	infile = open(file, 'rb')
	dicLst = pickle.load(infile) 
	infile.close()	
	
	return dicLst

def getJustice(dicLst, president):
	for k in dicLst:
		if dicLst[k]['pres'] == president:
			print("  {0:17}{1:4}".format(k, dicLst[k]['yrAppt']))
		else:
			pass

main()
